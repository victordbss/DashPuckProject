# Code qui gère tout les paramètres de la machine (variable) et le cablage

# Motor 1 => Moteur qui fait tourner le bras principal
# Sensor 26 => Capteur qui détecte le passage du bras robotique
# Servo 2 => Servo moteur qui bloque le bras (petit)
# Sensor 27 => Bouton qui lance le test


SENS_MOTEUR = 1 #1 ou -1
MOTOR_SPEED_TO_SENSOR = 60 # Vitesse du moteur qui tient le bras jusqu'au capteur (étape1)
BW_SENSOR_CHANGE_VALUE = 20000 # Valeur du capteur blanc et noir quand il détecte le passage du bras robotique
BUTTON_SENSOR_VALUE = 10000 # Valeur minimale qui ne détecte pas un appui sur le bouton
TIME_FROM_SENSOR_TO_SERVO = 0.03 # Temps que met le bras robotique à passer du capteur bw au servo qui le stoppe

STOP_SERVO_START_ANGLE = 180 # Angle du servo moteur bloqueur pour lequel il ne stoppe pas le chemin du bras robotique
STOP_SERVO_END_ANGLE = 120 # Angle du servo moteur bloqueur pour lequel il stoppe le bras robotique