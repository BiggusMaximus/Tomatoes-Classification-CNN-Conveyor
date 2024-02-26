import RPi.GPIO as GPIO
import time

# Define GPIO pins for motor control
DIR = 20
STEP = 21
CW = 1
CCW = 0

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set up motor direction (CW/CCW) and step mode (full, half, etc.)
GPIO.output(DIR, CW)  # Set direction: CW or CCW
delay = 0.0005  # Set the delay between steps (adjust for your motor)

# Set up steps per revolution for your motor
SPR = 200  # Steps per revolution

# Function to rotate stepper motor
def step(steps):
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

try:
    while True:
        steps = int(input("Enter number of steps (positive for CW, negative for CCW, 0 to stop): "))
        if steps == 0:
            break
        step(abs(steps))
except KeyboardInterrupt:
    GPIO.cleanup()
