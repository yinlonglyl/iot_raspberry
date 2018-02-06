#!/usr/bin/python3

import RPi.GPIO as GPIO
#import psutil
import time

RED = 5
#YELLOW = 6
#GREEN = 13

#Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(GREEN, GPIO.OUT)
#GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

try:
    while(1):
        #print("In")
        GPIO.output(RED, False)
        time.sleep(2*60)
        GPIO.output(RED, True)
        #GPIO.output(YELLOW, True)
        #GPIO.output(GREEN, True)
        time.sleep(20*60)
        GPIO.output(RED, False)
        #GPIO.output(YELLOW, False)
        #GPIO.output(GREEN, False)
        time.sleep(5*60)
except KeyboardInterrupt:
    print("Bye Bye")
    #GPIO.output(GREEN, False)
    #GPIO.output(YELLOW, False)
    GPIO.output(RED, False)

