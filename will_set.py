import paho.mqtt.client as mqtt
from threading import Timer
import time
import json

client =mqtt.Client("mizan0050")
broker= "broker.hivemq.com"
port=1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload))
    print('\n')


client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object 

dummyDeviceData = {
    "processor": "Intel(R) corei7-5500U CPU 2.40 GHz",
    "ram": "8.00 GB",
    "hdd": "500GB",
    "os": "widows XP",
    "internet_speed": "512 kbps",
    }


data = json.dumps(dummyDeviceData)
jsonData = json.loads(data)

# print (jsonData['pcmac'])
client.will_set("srdl/ds/9833000A33DD", payload="Offline", qos=1, retain=False)
client.connect(broker, port, 60)

print("connecting to broker")

# client.loop_start() #start the loop

# client.subscribe("sensor/data1") #receive the same data that are being published
# print "subscribed"

def publish():
    client.publish("srdl/ds/9833000A33DD", data )  # publish
    #client.publish("srdl/school2", data )  # publish
    Timer(2.0, publish).start() # publish every 2 seconds


publish() # initialise the function

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
client.loop_forever() # to maintain continuous network traffic flow with the broker

