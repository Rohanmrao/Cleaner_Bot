import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)

# Set up servo pins
base_pin = 11
shoulder_pin = 12
elbow_pin = 13
wrist_pitch_pin = 15
wrist_roll_pin = 16
gripper_pin = 18

GPIO.setup(base_pin, GPIO.OUT)
GPIO.setup(shoulder_pin, GPIO.OUT)
GPIO.setup(elbow_pin, GPIO.OUT)
GPIO.setup(wrist_pitch_pin, GPIO.OUT)
GPIO.setup(wrist_roll_pin, GPIO.OUT)
GPIO.setup(gripper_pin, GPIO.OUT)

# Set up PWM frequency
pwm_frequency = 50
base_pwm = GPIO.PWM(base_pin, pwm_frequency)
shoulder_pwm = GPIO.PWM(shoulder_pin, pwm_frequency)
elbow_pwm = GPIO.PWM(elbow_pin, pwm_frequency)
wrist_pitch_pwm = GPIO.PWM(wrist_pitch_pin, pwm_frequency)
wrist_roll_pwm = GPIO.PWM(wrist_roll_pin, pwm_frequency)
gripper_pwm = GPIO.PWM(gripper_pin, pwm_frequency)

# Set up PWM duty cycles for each servo
base_duty_cycle = 7.5
shoulder_duty_cycle = 7.5
elbow_duty_cycle = 7.5
wrist_pitch_duty_cycle = 7.5
wrist_roll_duty_cycle = 7.5
gripper_duty_cycle = 7.5

# Initialize servos to their default positions
base_pwm.start(base_duty_cycle)
shoulder_pwm.start(shoulder_duty_cycle)
elbow_pwm.start(elbow_duty_cycle)
wrist_pitch_pwm.start(wrist_pitch_duty_cycle)
wrist_roll_pwm.start(wrist_roll_duty_cycle)
gripper_pwm.start(gripper_duty_cycle)

# Define functions for moving each servo to a given angle
def move_base(angle):
    duty_cycle = (angle / 18) + 2.5
    base_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

def move_shoulder(angle):
    duty_cycle = (angle / 18) + 2.5
    shoulder_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

def move_elbow(angle):
    duty_cycle = (angle / 18) + 2.5
    elbow_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

def move_wrist_pitch(angle):
    duty_cycle = (angle / 18) + 2.5
    wrist_pitch_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

def move_wrist_roll(angle):
    duty_cycle = (angle / 18) + 2.5
    wrist_roll_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

def move_gripper(angle):
    duty_cycle = (angle / 18) + 2.5
    gripper_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

# Test the functions by moving each servo to a different angle
move_base(90)
move_shoulder(45)
move_elbow(90)
move_wrist_pitch(90)
move_wrist_roll(45)
move_gripper(90)

# Clean up GPIO pins
base_pwm.stop()
shoulder_pwm.stop()
elbow_pwm.stop()
wrist_pitch_pwm.stop()
wrist_roll_pwm.stop()
gripper_pwm.stop()
GPIO.cleanup()
