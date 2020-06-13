import paho.mqtt.client as mqtt


class Publish:

    def __init__(self, topic, value):
        self.topic = topic
        self.value = value
        self.client = mqtt.Client("python-pub")
        self.broker = "159.89.175.76"

        # def on_log(client, userdata, level, buf):
        #     print("log: " + buf)
        #
        # self.client.on_log = on_log

    def connect(self):
        print("Attempting to connect to broker", self.broker)
        self.client.connect(self.broker, 1883, 60)

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected OK")

        self.client.on_connect = on_connect

    def publish(self):
        def on_publish(client, userdata, result):
            print("Published")

        self.client.loop_start()
        self.client.on_publish = on_publish
        print(f"Attempting to publish {self.value} on {self.topic}")
        self.client.publish(self.topic, self.value)

        self.client.loop_stop()
