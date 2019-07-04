from agent_info import *
import time
import paho.mqtt.client as mqtt
import random
import re, uuid
import json



uuid.uuid4 # generating randorm number in base64
r = str(uuid.uuid4())
client = mqtt.Client(r)
broker = "broker.hivemq.com"
port = 1883

mac_addr = mac_addr()
gateway_ip = gateway_ip()
# print(mac_addr)
# keep_alive = {
# 	'mac_addr': mac_addr,
# 	'alive': True
# }
# keep_alive = str(keep_alive)

division_id = None
district_id = None
upazilla_id = None
lab_id = None



def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))


def on_message(client, userdata, message):
	print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
	check_topic(str(message.payload.decode("utf-8")))
	send_data_to_broker(str(message.payload.decode("utf-8")))

client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object

offline = {
 "status": "offline",
 "mac_addr": mac_addr,
 "gateway_ip": gateway_ip
}
offline_dump = json.dumps(offline)
client.will_set(f"srdl/res_offline/{mac_addr}/", payload = offline_dump, qos=1, retain=False)
client.connect(broker,port,60)
print ("connecting to broker")

# srdl/req_topic/d8:5d:e2:2f:de:bf/
# srdl/res_topic/d8:5d:e2:2f:de:bf/
# srdl/req_info/3/11/221/34/d8:5d:e2:2f:de:bf/
# srdl/res_info/3/11/221/34/d8:5d:e2:2f:de:bf/

# srdl/req_topic/68:f7:28:e3:f4:d4/
# srdl/res_topic/68:f7:28:e3:f4:d4/
# srdl/req_info/3/11/221/34/68:f7:28:e3:f4:d4/
# srdl/res_info/3/11/221/34/68:f7:28:e3:f4:d4/

# client.subscribe("srdl/req_info/test")

# client.subscribe("srdl/res_offline/d8:5d:e2:2f:de:bf/")

client.subscribe(f"srdl/res_topic/{mac_addr}/", 1)
client.subscribe(f"srdl/req_info", 1)
if district_id is None:
	print("Publish topic for address")
	# client.publish(f"srdl/req_topic/{mac_addr}/", str({"topic": 1}))
	topic = {"topic" : 1}
	topic_dump = json.dumps(topic)
	client.publish( f"srdl/req_topic/{mac_addr}/", topic_dump)



def check_topic(msg):
	global division_id, district_id, upazilla_id, lab_id
	if (division_id is None and district_id is None and upazilla_id is None and lab_id is None):
		data = json.loads(msg)
		topic_value = data.get("topic", "")
		
		if 'topic' in data and topic_value == 1:
			print("Address info receive from server")
			if 'division_id' in data:
				value = data.get("division_id", "")
				division_id = value
				print('division_id', value)

			if 'district_id' in data:
				value = data.get("district_id", "")
				district_id = value
				print('district_id', value)

			if 'upazilla_id' in data:
				value = data.get("upazilla_id", "")
				upazilla_id = value
				print('upazilla_id', value)

			if 'lab_id' in data:
				value = data.get("lab_id", "")
				lab_id = value
				print('lab_id', value)
			print('ok')
			client.subscribe(f"srdl/req_info/{division_id}/{district_id}/{upazilla_id}/{lab_id}/{mac_addr}/")
		else:
			print("Publish topic for address")
			# client.publish(f"srdl/req_topic/{mac_addr}/", str({"topic": 1}))
			topic = {"topic" : 1}
			topic_dump = json.dumps(topic)
			client.publish( f"srdl/req_topic/{mac_addr}/", topic_dump)
		print ("subscribed", f"srdl/req_info/{division_id}/{district_id}/{upazilla_id}/{lab_id}/{mac_addr}/")
		# district_id = "Dhaka"
	else:
		return True

def send_data_to_broker(msg):
	data = json.loads(msg)
	info_value = data.get("info", "")

	if 'info' in data and info_value == 1:
		print("Receive a request for send info")
		res_info = info(data)
		print(res_info)
		print(f"srdl/res_info/{division_id}/{district_id}/{upazilla_id}/{lab_id}/{mac_addr}/")
		res_info = json.dumps(res_info)
		client.publish(f"srdl/res_info/{division_id}/{district_id}/{upazilla_id}/{lab_id}/{mac_addr}/", res_info)

	
	

client.loop_forever() # to maintain continuous network traffic flow with the broker


