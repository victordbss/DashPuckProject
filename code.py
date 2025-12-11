from setup import *
import settings as stg
import time

#play_music("veridisquo")

auto_mode = False
release = True

#Etape qui ammène le bras jusqu'au capteur 
def step1() -> bool:
    motor1.set_speed(stg.MOTOR_SPEED_TO_SENSOR * stg.SENS_MOTEUR)
    while distance_sensor.get_distance() > stg.DISTANCE_SENSOR_DETECT_VALUE:
        print(distance_sensor.get_distance())
        time.sleep(0.01)
    return True



def step2() -> bool:
    x_value = 0
    motor_speed = 50
    while motor_speed < stg.MAX_SPEED:
        motor_speed = speed_fonction(x_value)
        motor1.set_speed(motor_speed * stg.SENS_MOTEUR)
        x_value += 1
        time.sleep(0.01)
        print(motor_speed)
    motor1.set_speed(100 * stg.SENS_MOTEUR)
    return True

def step3() -> bool:
    while distance_sensor.get_distance() > stg.DISTANCE_SENSOR_DETECT_VALUE:
        print(distance_sensor.get_distance())
        time.sleep(0.005)
    servo2.set_angle(stg.STOP_SERVO_END_ANGLE)
    time.sleep(stg.TIME_FROM_SENSOR_TO_SERVO)
    motor1.set_speed(0)
    time.sleep(1)
    servo2.set_angle(stg.STOP_SERVO_START_ANGLE)
    

def launch():
    if step1():
        print("step 1 done")
        
        if step2():
            print("step 2 done")
            
            step3()

def rotate(sens : int = 1):
    motor2.set_speed(stg.ANGLE_MOTOR2_SPEED * sens)
    time.sleep(stg.TIME_TO_ANGLE)
    motor2.set_speed(0)


while True:
    led4.value = auto_mode

    # Bouton qui change de mode
    if not button5.value and release:
        # Ajout d'un son
        auto_mode = not auto_mode
        play_music("jump_up")
        release = False
    else:
        time.sleep(0.2)
        
        release = True
        
    
    # Bouton qui fait tourner la machine à droite
    if not auto_mode and (not button6.value or not button7.value):
        if not button6.value:
            motor2.set_speed(stg.ANGLE_MOTOR2_SPEED)
        else:
            motor2.set_speed(stg.ANGLE_MOTOR2_SPEED * -1)
    else:
        motor2.set_speed(0)
    
    if not button8.value:
        if not auto_mode:
            launch()
        else:
            while True:
                if sensor26.value < stg.BW_SENSOR_CHANGE_VALUE:
                    launch()
                     # Ajuster le temps entre chaque tir
                else:
                    break
            time.sleep(0.5)
    
    time.sleep(0.05)
    

""" while True:
    user_input = input("Action :")
    if user_input == "launch":
        launch()
    elif user_input == "right":
        rotate(stg.SENS_MOTEUR)
    elif user_input == "left":
        rotate(-stg.SENS_MOTEUR)
    elif user_input == "test_servo":
        angle = input("angle :")
        servo2.set_angle(int(angle))
        time.sleep(1)
    elif user_input == "test_sensor":
        while True:
            print(sensor26.get_value())
            time.sleep(0.005)
            if sensor26.get_value() <= stg.BW_SENSOR_CHANGE_VALUE:
                print("detect")
    elif user_input == "distance_sensor":
        while True:
            print(distance_sensor.get_distance())
            time.sleep(0.05)

    time.sleep(0.5) """