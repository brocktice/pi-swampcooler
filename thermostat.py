#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

# Use board pin numbers for consistency across models
GPIO.setmode(GPIO.BOARD)

# Pinout
# Fan high: Board 3, relay in4
FANHIGH = 3

# Fan low: Board 5, relay in3
FANLOW = 5

# Pump: Board 7, Relay in2
PUMP = 7

# Drain: Board 11, Relay in1
DRAIN = 11

# Time to prime the pad in seconds
PRIMETIME=5

# Time to drain in seconds
DRAINTIME=5

PRIMED=0

def initialize():
    for pin in [FANHIGH, FANLOW, PUMP, DRAIN]:
        # note that GPIO.HIGH = relay OFF
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        
def relayOn(pin):
    GPIO.output(pin, GPIO.LOW)

def relayOff(pin):
    GPIO.output(pin, GPIO.HIGH)

def primePad():
    global PRIMED

    print "Priming pad."
    # fire up the pump for two minues to wet the pads
    relayOn(PUMP)
    time.sleep(PRIMETIME)
    print "Pad primed!"
    PRIMED=1

def drain():
    print "Draining."
    relayOn(DRAIN)
    time.sleep(DRAINTIME)
    relayOff(DRAIN)
    print "Draining complete."
    
def runHigh():
    global PRIMED

    if PRIMED == 0:
        primePad()
    print "Running on high"
    relayOff(FANLOW)
    relayOn(FANHIGH)

def runLow():
    global PRIMED
    if PRIMED == 0:
        primePad()
    print "Running on low"
    relayOff(FANHIGH)
    relayOn(FANLOW)

def runStop():
    global PRIMED
    PRIMED=0
    relayOff(FANHIGH)
    relayOff(FANLOW)
    relayOff(PUMP)

# program logic starts here
initialize()
    
# This will eventually be the main loop once thermistor is in use. For now just do a sample run
primePad()
runHigh()
time.sleep(5)
runLow()
time.sleep(5)
runStop()
drain()

print "Done running"

# cleanup when done
GPIO.cleanup()
