# Heartbeat Sensor #1
import time
from adafruit_circuitplayground.express import cpx


SAMPLING_INTERVAL = 0.02 
HEARTBEAT_THRESHOLD_HIGH = 205
HEARTBEAT_THRESHOLD_LOW = 100


heartbeat_count = 0
start_time = time.monotonic()

while True:
    
    z_acceleration = cpx.acceleration[2]

   
    if z_acceleration > 10.5:
        heartbeat_count += 1

    
    if time.monotonic() - start_time >= 10:
        
        average_bpm = (heartbeat_count / 10) * 60

        
        print("Average BPM:", average_bpm)

        
        if average_bpm > HEARTBEAT_THRESHOLD_HIGH:
            print("Average Heartbeat too high")
            cpx.pixels.fill((255, 0, 0))  # Red
        elif average_bpm < HEARTBEAT_THRESHOLD_LOW:
            print("Average Heartbeat too low")
            cpx.pixels.fill((255, 255, 0))  # Yellow
        else:
            cpx.pixels.fill((0, 255, 0))  # Green

        
        heartbeat_count = 0
        start_time = time.monotonic()

    time.sleep(0.1)



