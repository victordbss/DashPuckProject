from setup import *
import time

play_music("power_up")
tour = 0
tour_pass = False
servo2.set_angle(90)
while True:
    motor1.set_speed(70)
    if sensor26.get_value() <= 25000:
        if not tour_pass:
            tour += 1
        if tour >= 2:
            servo2.set_angle(180)
            motor1.set_speed(0)
            time.sleep(3)
            servo2.set_angle(90)
            time.sleep(1)
            tour = 0
        tour_pass = True
    else:
        tour_pass = False
    
    time.sleep(0.01)
    print(sensor26.get_value())
