#!/usr/bin/env python
# blink example from http://www.thirdeyevis.com/pi-page-2.php

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set pin # to header #
GPIO.setup(23,GPIO.OUT)

def Blink(numTimes, speed):
	for i in range(0, numTimes):
		print "Iteration: %g " % (i + 1) # print timer
		GPIO.output(23, True) # turn on
		time.sleep(speed) # wait
		GPIO.output(23, False) # turn off
		time.sleep(speed) # wait
	print "done :)" # print done after loop completes
	GPIO.cleanup()

iterations = raw_input("enter the total number of times to blink: ")
speed = raw_input("enter the length of each blink(seconds):")

Blink(int(iterations), float(speed)) # convert input types to nums and pass as params  

