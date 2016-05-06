#!/usr/bin/env python


import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

for pin in [3, 5, 7, 11]:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

for iteration in range(0,10):
    for pin in [3, 5, 7, 11]:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)

GPIO.cleanup()
