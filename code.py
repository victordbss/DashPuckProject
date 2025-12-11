from setup import *  
import settings as stg
import time

# play_music("veridisquo") 

# ------------------------
# Variables d'état globales
# ------------------------
auto_mode_enabled = False    # True : tir automatique, False : tir manuel
mode_button_released = True  # Permet de détecter un front descendant sur le bouton de mode

MAIN_LOOP_DELAY = 0.05       # Délai de base de la boucle principale (en s)


# ------------------------
# Fonctions de séquence de tir
# ------------------------

def load_puck_from_hopper() -> bool:
    """
    Amène un palais du réservoir dans le système d'expulsion
    en actionnant le servo pousseur (servo3).
    """
    servo3.set_angle(stg.PUSH_SERVO_REST_ANGLE)
    time.sleep(0.5)
    servo3.set_angle(stg.PUSH_SERVO_PUSH_ANGLE)
    return True


def move_arm_to_distance_sensor() -> bool:
    """
    Étape 1 : amène le bras jusqu'au capteur de distance (ultrason).
    Le moteur 1 tourne dans le sens de MOTOR1_DIRECTION jusqu'à ce que
    la distance mesurée soit inférieure au seuil configuré.
    """
    motor1.set_speed(stg.MOTOR1_APPROACH_SPEED * stg.MOTOR1_DIRECTION)

    while distance_sensor.get_distance() > stg.DISTANCE_SENSOR_DETECT_VALUE:
        print("Distance (approche) :", distance_sensor.get_distance())
        time.sleep(0.01)

    return True


def accelerate_arm_to_throw_speed() -> bool:
    """
    Étape 2 : rampe d'accélération du bras pour atteindre la vitesse de tir.
    On utilise une fonction logistique (calculate_speed_profile) pour augmenter
    progressivement la vitesse jusqu'à une valeur proche de 100.
    """
    step_index = 0
    motor_speed = 50  # Vitesse de départ

    while motor_speed < stg.MOTOR1_MAX_SPEED:
        motor_speed = calculate_speed_profile(step_index)
        motor1.set_speed(motor_speed * stg.MOTOR1_DIRECTION)
        step_index += 1
        time.sleep(0.01)
        print("Vitesse bras :", motor_speed)

    # Vitesse finale (léger "overdrive" pour le tir)
    motor1.set_speed(100 * stg.MOTOR1_DIRECTION)
    return True


def stop_arm_with_servo_and_reset() -> None:
    """
    Étape 3 : arrêt du bras à l'aide du servo bloqueur (servo2).
    - Attendre que le bras passe devant le capteur de distance.
    - Positionner le servo pour bloquer le bras.
    - Arrêter le moteur.
    - Remettre le servo dans sa position initiale.
    """
    # Attente du passage du bras devant le capteur ultrason
    while distance_sensor.get_distance() > stg.DISTANCE_SENSOR_DETECT_VALUE:
        print("Distance (fin de tir) :", distance_sensor.get_distance())
        time.sleep(0.005)

    # Bloquer le bras
    servo2.set_angle(stg.STOP_SERVO_BLOCK_ANGLE)
    time.sleep(stg.TIME_FROM_SENSOR_TO_SERVO)

    # Arrêter le moteur
    motor1.set_speed(0)
    time.sleep(1)

    # Libérer le bras
    servo2.set_angle(stg.STOP_SERVO_OPEN_ANGLE)


def launch_one_puck():
    """
    Exécute la séquence complète :
    1. Charger un palais depuis le réservoir.
    2. Amener le bras jusqu'au capteur de distance.
    3. Accélérer le bras jusqu'à la vitesse de tir.
    4. Stopper et réinitialiser le système.
    """
    if load_puck_from_hopper():
        if move_arm_to_distance_sensor():
            print("Étape 1 terminée")

            if accelerate_arm_to_throw_speed():
                print("Étape 2 terminée")
                stop_arm_with_servo_and_reset()


def rotate_platform(direction: int = 1):
    """
    Fait tourner la machine (plateforme) avec motor2 dans un sens donné,
    pendant un temps fixé par TIME_TO_ROTATE_SECTOR.
    direction : +1 ou -1
    """
    motor2.set_speed(stg.ROTATION_MOTOR_SPEED * direction)
    time.sleep(stg.TIME_TO_ROTATE_SECTOR)
    motor2.set_speed(0)


# ------------------------
# Gestion des commandes utilisateurs (boutons)
# ------------------------

def handle_mode_button():
    """
    Gère le bouton 5 qui permet de changer de mode (manuel <-> auto).
    Utilise un système de 'release' pour éviter de basculer plusieurs fois
    pendant un seul appui.
    """
    global auto_mode_enabled, mode_button_released

    # Bouton pressé (signal bas) et bouton considéré comme relâché auparavant
    if not button5.value and mode_button_released:
        auto_mode_enabled = not auto_mode_enabled
        play_music("jump_up")
        mode_button_released = False

    # Quand le bouton est relâché (signal haut), on autorise un nouveau toggle
    elif button5.value:
        mode_button_released = True


def handle_manual_rotation():
    """
    En mode manuel (auto_mode_disabled), les boutons 6 et 7
    font tourner la machine à droite ou à gauche.
    """
    if auto_mode_enabled:
        # En mode auto, aucune rotation manuelle
        motor2.set_speed(0)
        return

    # Bouton 6 : rotation à droite
    if not button6.value:
        motor2.set_speed(stg.ROTATION_MOTOR_SPEED)

    # Bouton 7 : rotation à gauche
    elif not button7.value:
        motor2.set_speed(-stg.ROTATION_MOTOR_SPEED)

    else:
        motor2.set_speed(0)


def handle_launch_button():
    """
    Gère le bouton 8 qui déclenche le tir :
    - En mode manuel : un seul tir.
    - En mode auto : tirs répétés tant que le réservoir n'est pas vide.
    """
    if button8.value:
        # Bouton non pressé
        return

    # Bouton pressé
    if not auto_mode_enabled:
        # Mode manuel : un seul tir
        launch_one_puck()
    else:
        # Mode automatique :
        # tant que le capteur du réservoir indique qu'il reste des palais,
        # on enchaîne les tirs.
        while reservoir_sensor.value < stg.RESERVOIR_EMPTY_THRESHOLD:
            launch_one_puck()
            # Ajouter ici un délai si nécessaire entre chaque tir
        time.sleep(0.5)


# ------------------------
# Boucle principale
# ------------------------

while True:
    # LED qui indique le mode auto (allumée = auto)
    led4.value = auto_mode_enabled

    # Gestion du changement de mode
    handle_mode_button()

    # Gestion de la rotation manuelle (si mode manuel)
    handle_manual_rotation()

    # Gestion des tirs (manuel / auto)
    handle_launch_button()

    # Petit délai pour éviter de saturer le CPU
    time.sleep(MAIN_LOOP_DELAY)


"""
# ------------------------
# Mode "debug" via la console (à activer si besoin)
# ------------------------
while True:
    user_input = input("Action : ")

    if user_input == "launch":
        launch_one_puck()

    elif user_input == "right":
        rotate_platform(stg.ROTATION_DIRECTION_CW)

    elif user_input == "left":
        rotate_platform(-stg.ROTATION_DIRECTION_CW)

    elif user_input == "test_servo":
        angle = int(input("Angle : "))
        servo2.set_angle(angle)
        time.sleep(1)

    elif user_input == "test_sensor":
        while True:
            print(reservoir_sensor.get_value())
            time.sleep(0.005)
            if reservoir_sensor.get_value() <= stg.RESERVOIR_EMPTY_THRESHOLD:
                print("Détection !")

    elif user_input == "distance_sensor":
        while True:
            print(distance_sensor.get_distance())
            time.sleep(0.05)

    time.sleep(0.5)
"""
