#
# Import required libraries
import RPi.GPIO as GPIO
import threading 
#workig prog for sending image and 
import boto3
import os
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import sendtodydb
#from tempVid import video
#------------------------AWS key------------------------
access_key ='AKIAS3U7UNUBJL3SEVGZ'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

#-----------------------------

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
mlx_shape = (24,32)

#-------HC-SR04 sensor
#----------------------------------------
# PINS MAPPING AND SETUP
# --------------------------------------------------------------------
echoPIN = 24
triggerPIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(echoPIN,GPIO.IN)
GPIO.setup(triggerPIN,GPIO.OUT)
GPIO.setwarnings(False)
# ---------------------------------------
Id=0
check=0
def temp():
    while True:
        try:
            mlx.getFrame(frame) # read MLX temperatures into frame var
            #print (frame)
            
            sorted_index_array = np.argsort(frame)
            sorted_array = frame[sorted_index_array]
#             print("Sorted array:", sorted_array)
#             break
            rslt = sorted_array[-25 : ]
            rsltneg = sorted_array[25 : ]
            pc=np.mean(rslt)
            pf=(((9.0/5.0)*np.mean(rslt))+32.0)
            pf=np.round(pf,1)
            rc=np.mean(rsltneg)
            rf=(((9.0/5.0)*np.mean(rsltneg))+32.0)
            rf=np.round(rf,1)
            mytemp=[pf,rf]
            break
        except ValueError:
            continue # if error, just read again
# print out the average temperature from the MLX90640
    
    return mytemp
    #print("array of temp : ", frame)  array of temp
 
# --------------------------------------------------------------------
# MAIN FUNCTIONS
# --------------------------------------------------------------------

def distance():
#   while True:
#     try:
     new_reading = False
     counter, distance, duration = 0,0,0

         # send trigger
     GPIO.output(triggerPIN, 0)
     time.sleep(0.000002)
     GPIO.output(triggerPIN, 1)
     time.sleep(0.000010)
     GPIO.output(triggerPIN, 0)
     time.sleep(0.000002)

     # wait for echo reading
     while GPIO.input(echoPIN) == 0:
       pass
       counter += 1
       if counter == 5000:
          new_reading = True
          break

     if new_reading:
        return False
     startT = time.time()

     while GPIO.input(echoPIN) == 1: pass
     feedbackT = time.time()

     # calculating distance
     if feedbackT == startT:
      distance = "N/A"
     else:
      duration = feedbackT - startT
      #soundSpeed/2 = 34300 /2*# cm/s* 0.0328084 ft/cm=562.66406
      distance = duration * 562.66406
      distance = round(distance, 1)
     time.sleep(0.2)
     #print ("Distance in ft: " + str(distance))
     #temp()
     
     return distance
#     except ValueError:
#             continue # if error, just read again
  
 # loop to output0
 
def loopp():
    global Id
    global check
    d = distance()
    mytemp=temp() #get temp
    pt= mytemp[0]
    rt=(mytemp[1]-1.8)
    rt=np.round(rt,1)
 ####--------condition to correct temp at all distance---------------------------------------   
        
    if (d>1 and d<=1.5):
        dif=3.2
        m=0.35
        c=(d-1)*10
        pt= pt+dif+m*c
    
    
    if (d>1.5 and d<=2):
        dif=4.6
        m=0.4
        c=(d-1.5)*10
        pt= pt+dif+m*c
    
    if (d>2 and d<=2.5):
        dif=6.2
        m=0.1
        c=(d-2)*10
        pt= pt+dif+m*c
    
    if (d>2.5 and d<=3):
        dif=6.4
        m=0.22
        c=(d-2.5)*10
        pt= pt+dif+m*c
    
    if (d>3 and d<=3.5):
        dif=7.3
        m=0.15
        c=(d-3)*10
        pt= pt+dif+m*c
    
    if (d>3.5 and d<=4):
        dif=7.9
        m=0.1
        c=(d-3.5)*10
        pt= pt+dif+m*c
    
    
    if (d>4 and d<=4.5):
        dif=8.3
        m=0.25
        c=(d-4)*10
        pt= pt+dif+m*c
    
    if (d>4.5 and d<=5): 
        dif=9.2
        m=0.18
        c=(d-4.5)*10
        pt= pt+dif+m*c
        
    if (d>5 and d<=5.5):
        dif=9.7
        m=0.1
        c=(d-5)*10
        pt= pt+dif+m*c
    if (d>3):
        rt=(mytemp[1]-1.8)
        rt=np.round(rt,1)
    
    pt=np.round(pt,1)
    
    if (pt<92):     #person not detected
        pt=0
###------------------------------------------------------------------------------------------    
    print("Room Temperature: %.2f F" %rt)
    print("Person's Temperature: %.2f F" %pt)
   
    camId=2
    sendtodydb.livedb(camId,rt,pt)
    if (d>1.5 and d<5.4):
        
      if (pt>94):    #flagged temp setup
        check +=1
        if check>=2:
            flag=1
            Id+=2
            sendtodydb.mydynamodb(Id,flag,rt,pt)
            flag=0
            check=0
            time.sleep(1)
    
#loopp()    
 