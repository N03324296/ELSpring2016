#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def blink(pin):
	for i in range(0,3):
		GPIO.output(pin,GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output(pin,GPIO.LOW)
    	time.sleep(0.5)
    time.sleep(5)
    for i in range(0,4):
		GPIO.output(pin,GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output(pin,GPIO.LOW)
    	time.sleep(0.5)
    time.sleep(5)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    blink(11)

GPIO.cleanup()