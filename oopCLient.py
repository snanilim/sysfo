import paho.mqtt.client as mqtt
import time

class refiner(object):
    def __init__(self,configpath="./sampleconfig.xml"):
        try:
            self.CONFIGPATH = configpath
            self.BROKER_IP = "broker.hivemq.com"

            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.BROKER_IP,1883,60)
            print(f"Connected to {0}, starting MQTT loop")
            self.client.loop_forever()
        except Exception as e:
            print("error", e)


    def on_message(self,client,userdata,msg):
        """MQTT Callback function for handling received messages"""
        print("message received!")
        print("msg", msg)


    def on_connect(self, client, userdata, flags, rc):
        print("connected!")
        self.client.subscribe("TRACED")

