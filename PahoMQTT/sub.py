import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client(client_id="foo123", clean_session=False)  # 加入client_id和clean_session 可以在重连成功获取到以前的消息
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 600)  # 600为keepalive的时间间隔
client.subscribe('fifa', qos=1)  # qos = 1
client.loop_forever()  # 一直保持连接