from setup import *
import settings as stg
import time

play_music("power_up")


#Etape qui ammène le bras jusqu'au capteur 
def step1():
    motor1.set_speed(stg.MOTOR_SPEED_TO_SENSOR)
    while sensor26.get_value() >= stg.BW_SENSOR_CHANGE_VALUE:
        time.sleep(0.01)
    motor1.set_speed(0)
