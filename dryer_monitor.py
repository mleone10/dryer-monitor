#!/usr/bin/env python3
import RPi.GPIO as GPIO

input_channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_channel, GPIO.IN)

def main():
    return isVibrating()

def isVibrating():
    return GPIO.input(input_channel)

if __name__ == '__main__':
    print(main())
