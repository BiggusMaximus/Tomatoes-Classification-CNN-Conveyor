from gpiozero import AngularServo
from time import sleep

# Define GPIO pins for servo control
SERVO1_PIN = 17
SERVO2_PIN = 22
SERVO3_PIN = 27


servo1 = AngularServo(SERVO1_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(SERVO2_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo3 = AngularServo(SERVO3_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    servo1.angle = 90
    servo2.angle = 90
    servo3.angle = 90
    sleep(2)
    servo1.angle = 0
    servo2.angle = 0
    servo3.angle = 0
    sleep(2)
    servo1.angle = -90
    servo2.angle = -90
    servo3.angle = -90
    sleep(2)