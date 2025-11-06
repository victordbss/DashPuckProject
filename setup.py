import wumons


# Init sensor
sensor26 = wumons.Sensor(wumons.board.GP26)
sensor27 = wumons.Sensor(wumons.board.GP27)
sensor28 = wumons.Sensor(wumons.board.GP28)

button_a = wumons.DigitalButton(wumons.board.GP18) # -> button_a.is_pressed()
button_b = wumons.DigitalButton(wumons.board.GP19) # -> button_b.is_pressed()

motor1 = wumons.DCMotor(wumons.board.GP20, wumons.board.GP21)
motor2 = wumons.DCMotor(wumons.board.GP10, wumons.board.GP11)
motor3 = wumons.DCMotor(wumons.board.GP14, wumons.board.GP15)
motor4 = wumons.DCMotor(wumons.board.GP12, wumons.board.GP13)

# Grands servo-moteurs
servo0 = wumons.Servo(wumons.board.GP0)
servo0.set_pulse_width_range(300,1900)
servo1 = wumons.Servo(wumons.board.GP1)
servo1.set_pulse_width_range(300,1900)

# Petits servo-moteurs
servo2 = wumons.Servo(wumons.board.GP2)
servo2.set_pulse_width_range(400,2400)
servo3 = wumons.Servo(wumons.board.GP3)
servo3.set_pulse_width_range(400,2400)

music_player = wumons.Music(wumons.board.GP9)

wumons_leds = wumons.NeoPixel(wumons.board.GP22, 2, brightness=0.5, auto_write=False)

def colour_from_rgb(r, g, b):
   r = round(min(100, max(0, r)) * 2.55)
   g = round(min(100, max(0, g)) * 2.55)
   b = round(min(100, max(0, b)) * 2.55)
   return (r << 16) | (g << 8) | b

def color_led(led_index : int = 0, rgb_color : tuple[int, int, int] = (0,0,0)):
    if led_index == 0 or led_index == 1:
        wumons_leds[led_index] = colour_from_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        wumons_leds.show()
    else:
        raise ValueError(f"L'index de la led entrée n'est pas correct : {led_index}")

def play_music(music_name : str):
    music_attr = music_name.upper()
    if hasattr(music_player, music_attr):
        music_player.play(getattr(music_player, music_attr))
    else:
        print(f"Musique {music_name} non trouvée")