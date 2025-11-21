from setup import *
import settings as stg
import time

#play_music("veridisquo")

# Etape qui ammène le bras jusqu'au capteur 
def step1() -> bool:
    motor1.set_speed(stg.MOTOR_SPEED_TO_SENSOR * stg.SENS_MOTEUR)
    while sensor26.get_value() >= stg.BW_SENSOR_CHANGE_VALUE:
        print(sensor26.get_value())
        time.sleep(0.01)
    return True

def step2() -> bool:
    motor_speed = 50
    motor1.set_speed(motor_speed * stg.SENS_MOTEUR)
    
    while motor_speed < 100:
        motor1.set_speed(motor_speed * stg.SENS_MOTEUR)
        motor_speed += 1
        time.sleep(0.005)
        print(motor_speed)

    return True

def step3() -> bool:
    time.sleep(0.5)
    while sensor26.get_value() >= stg.BW_SENSOR_CHANGE_VALUE:
        time.sleep(0.01)
    servo2.set_angle(stg.STOP_SERVO_END_ANGLE)
    time.sleep(stg.TIME_FROM_SENSOR_TO_SERVO)
    motor1.set_speed(0)
    time.sleep(1)
    servo2.set_angle(stg.STOP_SERVO_START_ANGLE)

while True:
    if sensor27.get_value() <= stg.BUTTON_SENSOR_VALUE:
        if step1():
            print("done")
            time.sleep(1)
            if step2():
                print("done")
                step3()

    time.sleep(0.5)