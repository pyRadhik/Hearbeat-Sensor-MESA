# Heartbeat Sensor #1
from adafruit_circuitplayground.express import cpx

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import time


breath_count = 0
start_time = prev_time = time.monotonic()
acceleration = float();

kbd = Keyboard(usb_hid.devices, timeout=10)
layout = KeyboardLayoutUS(kbd)

#will probably have errors, im editing in a txt file rn
filter = Filter.RadialFilter(.025, .5, 0.75, 1)

while True:
    acceleration = cpx.acceleration[2] - 9.81
    current_time = time.monotonic()

    #todo: filter acceleration
    acceleration = filter.filter(acceleration, current_time - prev_time)
    
    print((acceration,))
    
    if acceleration > .05:
        breath_count += 1
    
    
    if current_time - start_time >= 10:
        average_bpm = (breath_count / 10) * 60
        print("Average breath per minute:", average_bpm)

        #try to send bpm to pc as a keyboard
        layout.write(str(average_bpm) + " ", delay=.05)
        
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



