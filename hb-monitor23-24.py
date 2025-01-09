# Heartbeat Sensor #1
from adafruit_circuitplayground.express import cpx
import time

breath_count = 0
start_time = time.monotonic()

while True:
    z_acceleration = cpx.acceleration[2]
    
    total_acceleration = abs(x_float) + abs(y_float) + abs(z_float)
    
    if z_acceleration > 9.85:
        breath_count += 1
        
    current_time = time.monotonic()
    if current_time - start_time >= 10:
        average_bpm = (breath_count / 10) * 60
        print("Average breath per minute:", average_bpm)
        if average_bpm > 60:
            print("Respiratory rate is too high")
            cpx.pixels.fill((255,0,0))
        elif average_bpm < 30:
            print("Respiratory rate is too low")
            cpx.pixels.fill((255,255,0))
        else:
            print("Heartrate is normal.")
            cpx.pixels.fill((0,255,0))
    time.sleep(0.1)



