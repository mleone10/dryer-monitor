#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

input_channel = 17
SENSING_SECONDS_MAX = 300

class Waiting():
    def next(self):
        if isVibrating():
            return Sensing()
        else:
            return self

class Sensing():
    sensing_seconds_current = 0
    def next(self):
        if self.sensing_seconds_current == SENSING_SECONDS_MAX:
            return Drying()
        elif isVibrating():
            self.sensing_seconds_current += 1
            return self
        else:
            return Waiting()

class Drying():
    def next(self):
        if isVibrating():
            return self
        else:
            notify()
            return Waiting()

def main():
    state = Waiting()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_channel, GPIO.IN)

    while True:
        time.sleep(1)
        state = state.next()

def isVibrating():
    return GPIO.input(input_channel)

def notify():
    print("Sending text!")

if __name__ == '__main__':
    print(main())
