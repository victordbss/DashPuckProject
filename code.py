# Import the wumons library
import wumons
import time

# Init Sensors
wumons_sensor26 = wumons.Sensor(wumons.board.GP26)
wumons_sensor27 = wumons.Sensor(wumons.board.GP27)
wumons_sensor28 = wumons.Sensor(wumons.board.GP28)

wumons_motor1 = wumons.DCMotor(wumons.board.GP20, wumons.board.GP21)
wumons_motor2 = wumons.DCMotor(wumons.board.GP10, wumons.board.GP11)
wumons_motor3 = wumons.DCMotor(wumons.board.GP14, wumons.board.GP15)
wumons_motor4 = wumons.DCMotor(wumons.board.GP12, wumons.board.GP13)

wumons_leds = wumons.NeoPixel(wumons.board.GP22, 2, brightness=0.5, auto_write=False)

wumons_music_player = wumons.Music(wumons.board.GP9)

# Functions 
def colour_from_rgb(r, g, b):
   r = round(min(100, max(0, r)) * 2.55)
   g = round(min(100, max(0, g)) * 2.55)
   b = round(min(100, max(0, b)) * 2.55)
   return (r << 16) | (g << 8) | b

def launch():
    wumons_leds[0]=colour_from_rgb(0,1,0)
    wumons_leds[1]=colour_from_rgb(0,1,0)
    wumons_leds.show()
    wumons_motor1.set_speed(100)
    time.sleep(0.5)
    wumons_motor1.set_speed(0)
    wumons_leds[0]=colour_from_rgb(1,0,0)
    wumons_leds[1]=colour_from_rgb(1,0,0)
    wumons_leds.show()

button = None

wumons_music_player.play(wumons_music_player.JUMP_UP)

wumons_leds[0]=colour_from_rgb(1,0,0)
wumons_leds[1]=colour_from_rgb(1,0,0)
wumons_leds.show()
while True:

    button = wumons_sensor26.get_value()
    if button < 20000:
        launch()
