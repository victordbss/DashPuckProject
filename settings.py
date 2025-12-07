# Code qui gère tout les paramètres de la machine (variable) et le cablage

# Motor 1 => Moteur qui fait tourner le bras principal
SENS_MOTEUR = -1 #1 ou -1
MAX_SPEED = 90

# Moteur 2 => Moteur qui fait tourner toute la machine
# Sensor 26 => Capteur qui détecte si le réservoir est vide
BW_SENSOR_CHANGE_VALUE = 20000 # Valeur du capteur blanc et noir quand qu'il n'y a plus de palais

# Servo 2 => Servo moteur qui bloque le bras (petit)

# Led 4 => Led qui s'allume quand le mode auto est activé
# Button 5 => bouton qui change de mode
# Button 6 => bouton qui fait tourner la machine à droite
# Button 7 => bouton qui fait tourner la machine à gauche
# Button 8 => bouton qui active la séquence de lancement


#Capteur ultrason (port i2c)
DISTANCE_SENSOR_DETECT_VALUE = 10 # Valeur à laquelle le capteur ultrason détecte le passage du bras robotique

#Etape 1 : approche du bras jusqu'au capteur
MOTOR_SPEED_TO_SENSOR = 60 # Vitesse du moteur qui tient le bras jusqu'au capteur (étape1)
TIME_FROM_DISTANCE_SENSOR_TO_HOLE = 0.3 # Temps que met le bras pour passer du passage du capteur de distance j'usqu'à l'endroit ou tombe les palais


MAX_SPEED = 90

ANGLE_MOTOR2_SPEED = 70 # Vitesse du moteur qui fait tourner la machine
CLOCKWISE_ANGLE = 1 # Valeur qui gère le sens du moteur qui fait tourner la machine 
TIME_TO_ANGLE = 1 # Temps qu'il faut pour atteindre l'angle désirer
BUTTON_SENSOR_VALUE = 10000 # Valeur minimale qui ne détecte pas un appui sur le bouton
TIME_FROM_SENSOR_TO_SERVO = 0.15 # Temps que met le bras robotique à passer du capteur bw au servo qui le stoppe

STOP_SERVO_START_ANGLE = 180 # Angle du servo moteur bloqueur pour lequel il ne stoppe pas le chemin du bras robotique
STOP_SERVO_END_ANGLE = 120 # Angle du servo moteur bloqueur pour lequel il stoppe le bras robotique