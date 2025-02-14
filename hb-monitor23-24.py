# Heartbeat Sensor #1
from adafruit_circuitplayground.express import cpx

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import time
import math

class Filter:
    def __init__(self):
        self.prevVal = 0.0

    def filter(self, value, time):
        self.prevVal = value
        return value

class SimpleFilter(Filter):
    def __init__(self, innerRadius):
        super().__init__()
        self.iRadius = innerRadius

    def filter(self, value, time):
        if math.fabs(value - self.prevVal) <= self.iRadius:
            value = self.prevVal
        return super().filter(value, time)

class RadialFilter(SimpleFilter):
    def __init__(self, innerRadius, outerRadius, descentSpeed, smoothness):
        super().__init__(innerRadius)
        self.oRadius = outerRadius
        self.descentSpeed = descentSpeed
        self.smoothness = smoothness

    def filter(self, value, time):
        distance = self.prevVal - value
        #Cleaned up the math
        if math.fabs(distance) > self.iRadius and math.fabs(distance) <= self.oRadius:
            value = self.prevVal + (1 - self.descentSpeed) * self.oRadius * time * (math.atan(distance * self.smoothness) * 2.0/math.pi)
        if math.fabs(distance) > self.oRadius:
            if distance > 0:
                value -= self.oRadius
            else:
                value += self.oRadius
        return super().filter(value, time)


breath_count = 0
start_time = prev_time = time.monotonic()
acceleration = float();

kbd = Keyboard(usb_hid.devices, timeout=10)
layout = KeyboardLayoutUS(kbd)

#will probably have errors, im editing in a txt file rn
filter = RadialFilter(0.0, 0.5, .5, 1.0)

up = down = False

while True:
    acceleration = cpx.acceleration[2] - 9.81
    current_time = time.monotonic()

    #todo: filter acceleration
    acceleration = filter.filter(acceleration, current_time - prev_time)

    if acceleration > .05:
        up = True
    if acceleration < .25:
        down = True
        
    if up and down:
        breath_count += 1
        print("beat")
        up = False
        down = False

    if current_time - start_time >= 10:
        average_bpm = (breath_count / 10) * 60
        print("Average breath per minute:", average_bpm)

        #try to send bpm to pc as a keyboard
        #layout.write(str(average_bpm) + " ", delay=.05)
        print("Average Respiration Rate: ", average_bpm)
        if average_bpm > 60:
            print("Respiratory rate is too high")
            cpx.pixels.fill((50,0,0))

        elif average_bpm < 30:
            print("Respiratory rate is too low")
            cpx.pixels.fill((33, 33,0))

        else:
            print("Heartrate is normal.")
            cpx.pixels.fill((0,50,0))

        breath_count = 0
        start_time = time.monotonic()

    prev_time = current_time
    time.sleep(0.1)



