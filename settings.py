# Code qui gère tous les paramètres de la machine (variables) et le câblage logique

# ------------------------
# MOTEUR 1 : moteur du bras de tir
# ------------------------
MOTOR1_DIRECTION = -1      # +1 ou -1 selon le câblage
MOTOR1_MAX_SPEED = 90      # Vitesse max utilisée dans la rampe d'accélération

# ------------------------
# MOTEUR 2 : rotation de la machine (plateforme)
# ------------------------
ROTATION_MOTOR_SPEED = 70  # Vitesse du moteur qui fait tourner la machine
ROTATION_DIRECTION_CW = 1  # Sens horaire (ClockWise)
TIME_TO_ROTATE_SECTOR = 1  # Durée pour atteindre l'angle désiré (en s)

# ------------------------
# CAPTEUR RÉSERVOIR (sensor26)
# ------------------------
# Capteur qui détecte si le réservoir est vide (noir/blanc)
RESERVOIR_EMPTY_THRESHOLD = 20000  # Valeur au-dessus de laquelle on considère qu'il n'y a plus de palais

# ------------------------
# CAPTEUR ULTRASON (distance_sensor, port I2C)
# ------------------------
DISTANCE_SENSOR_DETECT_VALUE = 10  # Distance à laquelle le capteur détecte le passage du bras

# ------------------------
# ÉTAPE 1 : approche du bras jusqu'au capteur de distance
# ------------------------
MOTOR1_APPROACH_SPEED = 60               # Vitesse du moteur pendant l'approche
TIME_FROM_DISTANCE_SENSOR_TO_HOLE = 0.3  # Temps entre le capteur et la position de chute des palais

# ------------------------
# CAPTEUR NOIR/BLANC + SERVO DE BLOCAGE
# ------------------------
BUTTON_SENSOR_MIN_VALUE = 10000     # Valeur minimale pour considérer qu'il n'y a pas d'appui sur le bouton
TIME_FROM_SENSOR_TO_SERVO = 0.4    # Temps pour que le bras passe du capteur BW au servo qui le stoppe

STOP_SERVO_OPEN_ANGLE = 180         # Angle où le servo bloqueur NE bloque PAS le bras
STOP_SERVO_BLOCK_ANGLE = 120        # Angle où le servo bloqueur bloque le bras

# ------------------------
# SERVO POUSSEUR (réservoir → bras)
# ------------------------
PUSH_SERVO_REST_ANGLE = 100           # Position de repos
PUSH_SERVO_PUSH_ANGLE = 0         # Position qui pousse un palais dans le système

LED_PATERN = [[1,0,0], [0,1,0], [0,0,1]]
LED_LOOP_DELAY = 1

COLORS = [[100,0,0], [0,0,100]]
