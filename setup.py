import wumons
import board
import digitalio
import math
from wumons_i2c.dfr_urm09 import DFRobot_URM09

# ------------------------
# Fonction de profil de vitesse (rampe)
# ------------------------
def calculate_speed_profile(step_index: int) -> int:
    """
    Calcule une vitesse (0-100) suivant une fonction logistique,
    pour créer une rampe d'accélération progressive.
    step_index : entier qui augmente à chaque itération (0, 1, 2, ...)
    """
    return int((1 / (0.95 + math.exp(-0.015 * step_index))) * 100)

# ------------------------
# Capteur de distance (ultrason)
# ------------------------
# distance_sensor.get_distance() -> renvoie la distance en cm
distance_sensor = DFRobot_URM09(wumons.i2c)

# ------------------------
# LED (led4)
# ------------------------
# led4.value = True / False
led4 = digitalio.DigitalInOut(board.GP4)
led4.direction = digitalio.Direction.OUTPUT
deco_led1 = digitalio.DigitalInOut(board.GP8)
deco_led1 = digitalio.Direction.OUTPUT
deco_led2 = digitalio.DigitalInOut(board.GP9)
deco_led2 = digitalio.Direction.OUTPUT
deco_led3 = digitalio.DigitalInOut(board.GP10)
deco_led3 = digitalio.Direction.OUTPUT



# ------------------------
# Boutons (en digitalio)
# ------------------------
# Non pressé => True (pull-up)
button5 = digitalio.DigitalInOut(board.GP5)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.GP6)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

button7 = digitalio.DigitalInOut(board.GP7)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

button8 = digitalio.DigitalInOut(board.GP8)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.UP

# ------------------------
# Capteurs analogiques (réservoir, etc.)
# ------------------------
reservoir_sensor = wumons.Sensor(wumons.board.GP26)  # Anciennement sensor26
sensor27 = wumons.Sensor(wumons.board.GP27)
sensor28 = wumons.Sensor(wumons.board.GP28)

# ------------------------
# Boutons Wukong (facile à lire via .is_pressed())
# ------------------------
button_a = wumons.DigitalButton(wumons.board.GP18)  # -> button_a.is_pressed()
button_b = wumons.DigitalButton(wumons.board.GP19)  # -> button_b.is_pressed()

# ------------------------
# Moteurs DC
# ------------------------
# motor1 : moteur qui fait tourner le bras principal
motor1 = wumons.DCMotor(wumons.board.GP20, wumons.board.GP21)

# motor2 : moteur qui fait tourner la machine (plateforme)
motor2 = wumons.DCMotor(wumons.board.GP10, wumons.board.GP11)

motor3 = wumons.DCMotor(wumons.board.GP14, wumons.board.GP15)
motor4 = wumons.DCMotor(wumons.board.GP12, wumons.board.GP13)

# ------------------------
# Servo-moteurs
# ------------------------
# Grands servos
servo0 = wumons.Servo(wumons.board.GP0)
servo0.set_pulse_width_range(300, 1900)

servo1 = wumons.Servo(wumons.board.GP1)
servo1.set_pulse_width_range(300, 1900)

# Petits servos
servo2 = wumons.Servo(wumons.board.GP2)
servo2.set_pulse_width_range(400, 2400)

servo3 = wumons.Servo(wumons.board.GP3)
servo3.set_pulse_width_range(400, 2400)

# ------------------------
# Musique & LEDs NeoPixel
# ------------------------
music_player = wumons.Music(wumons.board.GP9)

wumons_leds = wumons.NeoPixel(
    wumons.board.GP22,
    2,
    brightness=0.5,
    auto_write=False
)

def colour_from_rgb(r: int, g: int, b: int) -> int:
    """
    Convertit des pourcentages (0-100) R, G, B en valeur 24 bits pour les NeoPixels.
    """
    r = round(min(100, max(0, r)) * 2.55)
    g = round(min(100, max(0, g)) * 2.55)
    b = round(min(100, max(0, b)) * 2.55)
    return (r << 16) | (g << 8) | b

def set_led_color(led_index: int = 0, rgb_color: tuple[int, int, int] = (0, 0, 0)):
    """
    Allume une LED NeoPixel avec la couleur donnée (R, G, B en pourcentages 0-100).
    led_index : 0 ou 1
    """
    if led_index in (0, 1):
        wumons_leds[led_index] = colour_from_rgb(
            rgb_color[0], rgb_color[1], rgb_color[2]
        )
        wumons_leds.show()
    else:
        raise ValueError(f"Index de LED invalide : {led_index}")

def play_music(music_name: str):
    """
    Joue une musique définie dans l'objet music_player.
    music_name : nom sous forme de string, converti en MAJUSCULE pour matcher les attributs.
    """
    music_attr = music_name.upper()
    if hasattr(music_player, music_attr):
        music_player.play(getattr(music_player, music_attr))
    else:
        print(f"Musique {music_name} non trouvée")
