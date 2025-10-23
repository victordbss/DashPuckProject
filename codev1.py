# Import the wumons library
import wumons
import time
#   Init Sensors
wumons_sensor26 = wumons.Sensor(wumons.board.GP26)
wumons_sensor27 = wumons.Sensor(wumons.board.GP27)
wumons_sensor28 = wumons.Sensor(wumons.board.GP28)

wumons_motor1 = wumons.DCMotor(wumons.board.GP20, wumons.board.GP21)
wumons_motor2 = wumons.DCMotor(wumons.board.GP10, wumons.board.GP11)
wumons_motor3 = wumons.DCMotor(wumons.board.GP14, wumons.board.GP15)
wumons_motor4 = wumons.DCMotor(wumons.board.GP12, wumons.board.GP13)

wumons_servo0 = wumons.Servo(wumons.board.GP0)
wumons_servo1 = wumons.Servo(wumons.board.GP1)
wumons_servo2 = wumons.Servo(wumons.board.GP2)
wumons_servo3 = wumons.Servo(wumons.board.GP3)

wumons_servo0.set_pulse_width_range(300,1900)

wumons_music_player = wumons.Music(wumons.board.GP9)

tour = 0
tour_pass = False

wumons_music_player.play(wumons_music_player.POWER_UP)

while True:
    print(wumons_sensor26.get_value())
    if wumons_sensor26.get_value() >= 10000:
        tour_pass = True
        wumons_motor1.set_speed(100)
    else:
        if tour_pass:
            tour_pass = False
            tour += 1
            if tour == 2:
                tour = 0
                time.sleep(0.15)
                wumons_motor1.set_speed(0)
                wumons_servo0.set_angle(0)
                time.sleep(0.75)
                wumons_motor1.set_speed(-60)
                time.sleep(0.25)
                wumons_motor1.set_speed(0)
                wumons_servo0.set_angle(180)
                
                time.sleep(1)
                wumons_motor1.set_speed(60)
                time.sleep(0.15)
                wumons_motor1.set_speed(0)
                time.sleep(1)
        
    time.sleep(0.02)