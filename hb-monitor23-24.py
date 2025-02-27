# Heartbeat Sensor
from adafruit_circuitplayground.express import cpx

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import KeyCode
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
        if abs(value - self.prevVal) <= self.iRadius:
            value = self.prevVal
        return super().filter(value, time)

class RadialFilter(SimpleFilter):
    def __init__(self, innerRadius, outerRadius, descentSpeed, smoothness):
        super().__init__(innerRadius)
        self.oRadius = outerRadius
        self.descentSpeed = descentSpeed
        self.smoothness = smoothness

    def filter(self, value, time):
        distance = value - self.prevVal
        abs_distance = abs(distance)

        if abs_distance > self.iRadius:
            if abs_distance <= self.oRadius:
                # Smooth transition using atan-based function
                adjustment = (1 - self.descentSpeed) * self.oRadius * time * (math.atan(distance * self.smoothness) * 2.0 / math.pi)
                value = self.prevVal + adjustment
            else:
                # If change is too large, limit the adjustment
                value = value - math.copysign(self.oRadius, distance)

        return super().filter(value, time)


breath_count = 0
start_time = prev_time = time.monotonic()
acceleration = float()

kbd = Keyboard(usb_hid.devices, timeout=10)
layout = KeyboardLayoutUS(kbd)

#TODO: numbers need to be altered still
filter = RadialFilter(0.0, 0.5, .5, 1.0)

up = down = False

while True:
    acceleration = cpx.acceleration[2] - 9.81
    current_time = time.monotonic()

    #filters acceleration
    acceleration = filter.filter(acceleration, current_time - prev_time)

    #TODO: threshold values need to be altered
    if acceleration > .15:
        up = True
    if acceleration < .2:
        down = True
        
    if up and down:
        breath_count += 1
        print("beat")
        up = False
        down = False

    if current_time - start_time >= 10:
        average_bpm = breath_count * 6 #(breath_count / 10) * 60
        print("Average breath per minute:", average_bpm)

        #try to send bpm to pc as a keyboard
        #layout.write(str(average_bpm)", delay=.05)
        #kbd.press(Keycode.ENTER)
        #kbd.release_all()
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



