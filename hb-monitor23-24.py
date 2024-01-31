# hearbeat sensor 1
from adafruit_circuitplayground.express import cpx
import board
import time
movement_threshold = 5
sample_interval = 0.1
trigger = False
heartbeat = 0
start_time = time.monotonic()

while True:
    x_float, y_float, z_float = cpx.acceleration 
    total_acceleration = abs(x_float) + abs(y_float) + abs(z_float)
    if total_acceleration > movement_threshold:
        heartbeat += 1
    current_time = time.monotonic()
    if current_time - start_time >= 10:
        
        average_heartbeat = heartbeat * 6
        if average_heartbeat > 205:
            print("Baby's heart rate is too high")
            print(average_heartbeat)
        elif average_heartbeat < 100:
            print("Baby's heart rate is too low")
            print(average_heartbeat)
        else 
            print("Heartrate is normal.")
        if trigger = True
            # put code for playing sound with speaker input
            # put code for lighting up less (ideally blinking)
            
        heartbeat = 0
        current_time = start_time
    print("Average Heartbeat per minute:", average_beat)
    time.sleep(5)
