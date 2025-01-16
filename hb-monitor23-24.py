# Heartbeat Sensor #1
from adafruit_circuitplayground.express import cpx
import time

breath_count = 0
start_time = time.monotonic()

SP = 9.8
PV = float()
dx = float()
integral = float()
derivative = float()
error = float()

while True:
    PV = cpx.acceleration[2]
    current_time = time.monotonic()
    
    
    integral = (current_time - start_time) / 2 * (dx + SP - PV)
    derivative = (SP - PV - dx) / (current_time - start_time)
    
    dx = SP - PV
    
    error = integral + derivative + dx;
    
    print((error,))
    #print((PV,))
    
    

    if PV > 9.85:
        breath_count += 1

    
    
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
            
        breath_count = 0
        start_time = time.monotonic()
        
        
    time.sleep(0.1)



