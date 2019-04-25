#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

# This is the Publisher

client = mqtt.Client()
client.connect("broker.hivemq.com",1883,60)


client.loop_start()
while True:
    client.publish("topic/test", "Hello world!")
    time.sleep(10)
client.disconnect()
