# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from datetime import datetime
from time import sleep
from random import uniform
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import math
import distwidcam
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    #print ("Connected to AWS")
    connflag = True
    #print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str
    
 
 
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
def frame2db():
 mqttc = paho.Client()                                       # mqttc object
 mqttc.on_connect = on_connect                               # assign on_connect func
 mqttc.on_message = on_message                               # assign on_message func
 awshost = "a2icglxc0k8973-ats.iot.us-west-2.amazonaws.com"      # Endpoint
 awsport = 8883                                              # Port no.   
 clientId = "mything"                                     # Thing_Name
 thingName = "camwithdistSensor"                                    # Thing_Name
 caPath = "/home/pi/Videos/root-ca.pem"                                      # Root_CA_Certificate_Name
 certPath = "/home/pi/Videos/certificate.pem.crt"                            # <Thing_Name>.cert.pem
 keyPath = "/home/pi/Videos/private.pem.key"                          # <Thing_Name>.private.key
 mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 mqttc.loop_start()                                          # Start the loop
 Id = 0
 i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
 mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
 mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
 frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
 mlx_shape = (24,32)
 mlx.getFrame(frame)
 frame =frame *(9.0/5.0)+32        
 frame=np.round(frame,1)
 frame=np.flipud(frame)
 print("frame")
 d=distwidcam.distance()
 if (d>1 and d<=1.5):
        dif=3.2
        m=0.35
        c=(d-1)*10
        frame= frame+dif+m*c
    
    
 if (d>1.5 and d<=2):
        dif=4.6
        m=0.4
        c=(d-1.5)*10
        frame= frame+dif+m*c
    
 if (d>2 and d<=2.5):
        dif=6.2
        m=0.1
        c=(d-2)*10
        frame= frame+dif+m*c
    
 if (d>2.5 and d<=3):
        dif=6.4
        m=0.22
        c=(d-2.5)*10
        frame= frame+dif+m*c
    
 if (d>3 and d<=3.5):
        dif=7.3
        m=0.15
        c=(d-3)*10
        frame= frame+dif+m*c
    
 if (d>3.5 and d<=4):
        dif=7.9
        m=0.1
        c=(d-3.5)*10
        frame= frame+dif+m*c
    
    
 if (d>4 and d<=4.5):
        dif=8.3
        m=0.25
        c=(d-4)*10
        frame= frame+dif+m*c
    
 if (d>4.5 and d<=5): 
        dif=9.2
        m=0.18
        c=(d-4.5)*10
        frame= frame+dif+m*c
        
 if (d>5 and d<=5.5):
        dif=9.7
        m=0.1
        c=(d-5)*10
        frame= frame+dif+m*c
 
 temperature = np.mean(frame)
        
 lists = frame.tolist() #numpy array converted to list to make it work with json.dumps
 messageJson = json.dumps(lists)
        #timestamp = datetime.datetime.now()
 #idied the camera with id
 #id =0 for cam 1
 #id =1 for cam 2
 # and so on
 id ="0" 
        
        
 cat ='{"temperature":'+str(temperature)+', "id": '+' "'+id+'" , '+'"frame":'+messageJson+' }'
  
 #print (id)
 print (messageJson)
 mqttc.publish ("hem",cat,1)
   
         
         
        
 
 
