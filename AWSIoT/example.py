"""
使用AWS的 MQTT_SDK
"""
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


mqtt_client = MQTTClient(str(uuid.uuid1()))
mqtt_client1 = MQTTClient(str(uuid.uuid1()))


def callback(client, userdata, message):
    print(client)
    print(userdata)
    print(message.topic)
    print(message.payload.decode())


mqtt_client.subscribe('/test', 1, callback)
while not mqtt_client.is_connect:
    time.sleep(1)
mqtt_client1.publish("/test", 'test', 1)
time.sleep(3)
