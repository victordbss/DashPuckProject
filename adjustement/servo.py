from setup import *
import settings as stg
import time


while True:
    angle = int(input("angle :"))
    servo2.set_angle(angle)
    time.sleep(1)