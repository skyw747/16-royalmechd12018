import RPi.GPIO as GPIO
import time
import os
from time import sleep
GPIO.setmode(GPIO.BCM)
pin=4
GPIO.setup(pin,GPIO.IN)
time.sleep(1)
def takesnap():
        os.system("fswebcam -F 4 /home/dl118/thennavan/program/ten.jpg")
        return
while True:
    if GPIO.input(pin):
        print("Motion Detected")
        time.sleep(1)
     

    else:
        print("Nothing......")
        time.sleep(1)

		
		
