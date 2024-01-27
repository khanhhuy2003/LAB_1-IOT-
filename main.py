import sys
import time
import random

from Adafruit_IO import MQTTClient
AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "khanhhuy03"
AIO_KEY = "aio_Sztn89l5YFaY6uF9z21A7RZJXRD2"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
     client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        print("Random data is publishing...")
        temp = random.randint(10,20)
        client.publish("cambien1", temp)
        humid =random.randint(30,60)
        client.publish("cambien2", humid)
        light =random.randint(1000,5000)
        client.publish("cambien3",light)
    time.sleep(1)
    pass