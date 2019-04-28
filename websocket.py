import sys
import paho.mqtt.client as mqtt
import time

def on_connect(mqttc, obj, flags, rc):
    
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print('okk', msg.qos)
    mqttc.publish("web/hello/next", "Hello worldsss!")
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_click(mqttc, obj, flags, rc):
    print("click: "+str(rc))

def on_publish(mqttc, obj, mid):
    
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    # mqttc.publish("web/hello", "Hello worldsss!")
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client(transport='websockets')   

mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.on_click = on_click

mqttc.connect("broker.hivemq.com", 8000, 60)

mqttc.subscribe("web/hello", 1)

mqttc.loop_forever()