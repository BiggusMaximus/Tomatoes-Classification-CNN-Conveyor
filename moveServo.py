import RPi.GPIO as GPIO
import time

# Define GPIO pins for servo control
SERVO1_PIN = 17
SERVO2_PIN = 22
SERVO3_PIN = 27

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO1_PIN, GPIO.OUT)
GPIO.setup(SERVO2_PIN, GPIO.OUT)
GPIO.setup(SERVO3_PIN, GPIO.OUT)

# Set up PWM for servo control
servo1 = GPIO.PWM(SERVO1_PIN, 50)  # GPIO 17 for PWM with 50Hz
servo2 = GPIO.PWM(SERVO2_PIN, 50)  # GPIO 18 for PWM with 50Hz
servo3 = GPIO.PWM(SERVO3_PIN, 50)  # GPIO 27 for PWM with 50Hz

# Start PWM
servo1.start(0)
servo2.start(0)
servo3.start(0)

# Function to set servo angle
def set_angle(servo, angle):
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    servo.ChangeDutyCycle(0)

try:
    angle = 330  # Angle to move all servos to
    
    set_angle(servo1, angle)
    set_angle(servo2, angle)
    set_angle(servo3, angle)

except KeyboardInterrupt:
    servo1.stop()
    servo2.stop()
    servo3.stop()
    GPIO.cleanup()
