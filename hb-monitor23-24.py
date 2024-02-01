from adafruit_circuitplayground.express import cpx
import time

movement_threshold = 0.01
sample_interval = 0.1
trigger = False
heartbeat = 0
start_time = time.monotonic()
current_time = start_time

while True:
    x, y, z = cpx.acceleration 
    total_acceleration = abs(x) + abs(y) + abs(z)
    if total_acceleration > movement_threshold:
        heartbeat += 1
        
    if time.monotonic() - start_time >= 10:
        average_heartbeat = heartbeat * 6
        heartbeat = 0
        start_time = time.monotonic()
        if average_heartbeat > 205:
            print("Baby's heart rate is too high")
            print("Average Heartbeat per minute:", average_heartbeat, "bpm")
            cpx.pixels.fill((127, 0, 0))
        elif average_heartbeat < 100:
            print("Baby's heart rate is too low")
            print("Average Heartbeat per minute:", average_heartbeat, "bpm")
            cpx.pixels.fill((150, 127, 0))
        else:
            print("Heartrate is normal.")
            print("Average Heartbeat per minute:", average_heartbeat, "bpm")
            cpx.pixels.fill((0, 255, 0))
    time.sleep(5)


