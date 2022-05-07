
# Import required libraries
import RPi.GPIO as GPIO
import time

# --------------------------------------------------------------------
# PINS MAPPING AND SETUP
# --------------------------------------------------------------------

echoPIN = 24
triggerPIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(echoPIN,GPIO.IN)
GPIO.setup(triggerPIN,GPIO.OUT)

# --------------------------------------------------------------------
# MAIN FUNCTIONS
# --------------------------------------------------------------------

def distance ():
 new_reading = False
 counter = 0
 distance = 0
 duration = 0

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
 return distance

# --------------------------------------------------------------------
# MAIN LOOP
# --------------------------------------------------------------------

try:
 while True:
  print (" Distance in ft: " + str(distance())+ "   ", end='\r')
  print ("")
  
except KeyboardInterrupt:
 print('interrupted!')
 GPIO.cleanup()



