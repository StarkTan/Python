import json
import urllib.request
import urllib.parse
import os
import threading
import time
import uuid

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class MQTTClient:
    STATIC_DIR = os.path.join(os.getcwd(), "private_file")
    HOST = "a2xpq0ku700e52-ats.iot.us-east-1.amazonaws.com"
    PORT = 8883

    CA_CRT = os.path.join(STATIC_DIR, "root-CA.crt")
    PRIVATE_KEY = os.path.join(STATIC_DIR, "Gateway.private.key")
    CERT_PEM = os.path.join(STATIC_DIR, "Gateway.cert.pem")

    CONNECT_TIMEOUT = 10
    OPERATION_TIMEOUT = 5

    def __init__(self, client_id):

        self.client = AWSIoTMQTTClient(client_id)
        self.client.configureEndpoint(self.HOST, self.PORT)

        self.client.configureCredentials(self.CA_CRT, self.PRIVATE_KEY, self.CERT_PEM)
        self.client.configureOfflinePublishQueueing(-1)
        self.client.configureDrainingFrequency(2)
        self.client.configureConnectDisconnectTimeout(self.CONNECT_TIMEOUT)
        self.client.configureMQTTOperationTimeout(self.OPERATION_TIMEOUT)
        #
        self.subscribe_topic_set = set()
        self.is_connect = False
        threading.Thread(target=self.connect).start()

    def publish(self, topic, payload, qos):
        if not self.is_connect:
            # print("Network exception, publishing failed.")
            return
        self.client.publish(topic, payload, qos)

    def subscribe(self, topic, qos, call_back):
        if not self.is_connect:
            self.subscribe_topic_set.add((topic, qos, call_back))
            return
        self.client.subscribe(topic, qos, call_back)

    def connect(self):
        while True:
            try:
                self.client.connect()
                self.is_connect = True
                for item in self.subscribe_topic_set:
                    topic, qos, call_back = item
                    self.client.subscribe(topic, qos, call_back)
                break
            except Exception:
                time.sleep(2)
                pass


def get(url, data, headers=None):
    if headers is None:
        headers = {}
    params = urllib.parse.urlencode(data)
    request = urllib.request.Request("%s?%s" % (url, params), method='GET')
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request)


def post(url, data, headers=None):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='POST')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


def put(url, data, headers=None):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='PUT')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


def delete(url, data, headers=None):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='DELETE')
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


mqtt_client = MQTTClient(str(uuid.uuid1()))
mqtt_client1 = MQTTClient(str(uuid.uuid1()))


def callback(client, userdata, message):
    msg = message.payload.decode()
    print(msg)
    jsonObj = json.loads(msg)
    msg_id = jsonObj['messageId']
    res_topic = message.topic + '/' + msg_id
    if 'handle' in jsonObj and jsonObj['handle'] == 'http':
        request = jsonObj['request']
        if request is None:
            return
        method = request['method']
        params = request['params']
        url = 'http://192.168.1.1:8000' + request['uri']
        headers = {'Authorization': 'Basic aGltYTAwNDoxMjM0NTY='}
        mqtt_response = None
        if method == 'GET':
            response = get(url, params, headers)
            mqtt_response = response.read().decode('utf-8')
        if method == 'POST':
            response = post(url, params, headers)
            mqtt_response = response.read().decode('utf-8')
        if method == 'PUT':
            response = put(url, params, headers)
            mqtt_response = response.read().decode('utf-8')
        if method == 'DELETE':
            response = delete(url, params, headers)
            mqtt_response = response.read().decode('utf-8')
        res_dic = {'message': mqtt_response}
        mqtt_client1.publish(res_topic, json.dumps(res_dic), 1)


mqtt_client.subscribe('http/mqtt', 1, callback)
while not mqtt_client.is_connect:
    time.sleep(1)
print("mqtt client connect succeed")
while True:
    time.sleep(10)
