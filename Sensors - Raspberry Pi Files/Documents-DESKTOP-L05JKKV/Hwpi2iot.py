import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import datetime
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep

myMQTTClient = AWSIoTMQTTClient("heatwavepi")
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a3kn89cefc1q2t-ats.iot.us-east-2.amazonaws.com", 8883) #Provide your AWS IoT Core endpoint (Example: "abcdef12345-ats.iot.us-east-1.amazonaws.com")

myMQTTClient.configureCredentials("/home/pi/Downloads/root-ca.pem", "/home/pi/Downloads/private.pem.key", "/home/pi/Downloads/certificate.pem.crt") #Set path for Root CA and unique device credentials (use the private key and certificate retrieved from the logs in Step 1)
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)


i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
mlx_shape = (24,32)
myid=1
 
print("Connecting...")
myMQTTClient.connect()
myMQTTClient.publish("heatwave","connected",0)
while True:
   myid=1
   mlx.getFrame(frame)
   temperature = np.mean(frame)
   lists = frame.tolist() #numpy array converted to list to make it work with json.dumps
   messageJson = json.dumps(lists)
   timestamp = datetime.datetime.now()
   
   
   cat ='{"myid":'+str(myid)+',"temperature":'+str(temperature)+',"timestamp": '+' " '+str(timestamp)+' " , '+'"frame":'+messageJson+' }'
  
   print (timestamp)
   print (messageJson)
   myMQTTClient.publish ("heatwave",cat,0)
    
   
   sleep(2)



