import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK")


def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_message(client, userdata, msg):
    print("message received ", str(msg.payload.decode("utf-8")))
    print("message topic=", msg.topic)


broker = "159.89.175.76"
client = mqtt.Client("python-sub")
client.connect(broker, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log

print("connecting to broker", broker)
client.subscribe("nou/#")
print("subscribed")
client.loop_forever()
