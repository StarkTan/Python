import paho.mqtt.client as paho
import ssl
from time import sleep
from random import uniform


connflag = False


def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
# mqttc.on_log = on_log

awshost = "a2xpq0ku700e52-ats.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "myThingName"
thingName = "myThingName"
caPath = "private_file/root-CA.crt"
certPath = "private_file/Gateway.cert.pem"
keyPath = "private_file/Gateway.private.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while 1==1:
    sleep(0.5)
    if connflag == True:
        tempreading = uniform(20.0,25.0)
        mqttc.publish("temperature", tempreading, qos=1)
        print("msg sent: temperature " + "%.2f" % tempreading )
    else:
        print("waiting for connection...")