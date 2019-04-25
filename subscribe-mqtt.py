import paho.mqtt.client as mqtt
import time
import logging

logging.getLogger().setLevel(logging.INFO)
broker = "broker.hivemq.com"
port = 1883

def on_log(client, userdata, level, buf):
    logging.info('buf')
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        logging.info("connected ok")
    else:
        logging.info("bad connection return code = " +  str(rc))
        client.loop_stop()
def on_disconnect(client, userdata, rc):
    logging.info("clint disconnected ok")
def on_publish(client, userdata, mid):
    logging.info("In on_pub callbac mid = " + str(mid))
def on_subscribe(client, userdata, mid, granted_qos):
    logging.info('subscribed')
def on_message(client, userdata, message):
    topic = message.topic
    msgr = str(message.payload.decode("utf-8"))
    msgr = "Message Received " + msgr
    logging.info(msgr)
def reset():
    ret = client.publish("house/bulb1", "", 0, True)



mqtt.Client.connected_flag = False
client = mqtt.Client("python 1")

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(broker)

client.loop_start()
while not client.connected_flag:
    logging.info("In Wait Loop")
    time.sleep(1)
time.sleep(3)
ret = client.publish("house/bulb1", "test message 0", 0, True)
logging.info("Publish return " + str(ret))
ret = client.publish("house/bulb1", "test message 1", 1)
logging.info("Publish return " + str(ret))
ret = client.publish("house/bulb1", "test message 2", 2)
logging.info("Publish return " + str(ret))

time.sleep(3)
client.subscribe("house/bulb1", 2)
reset()
time.sleep(10)
client.loop_stop()
client.disconnect()
