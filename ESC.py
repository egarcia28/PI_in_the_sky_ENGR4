import pulseio
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from adafruit_motor import servo
import time

def calibrateESC(esc, escSpeedPin):
    # ESC Calibration requires you to start out high, then adjust to low and wait for beeps and then power off
    escSpeed = getAngle(escSpeedPin)
    esc.angle = escSpeed

# Brushless Setup
escOut1 = pulseio.PWMOut(board.GP1, duty_cycle=0, frequency=50)
motor1 = servo.Servo(escOut1, min_pulse=1000, max_pulse=2000)


# Uncomment for calibration of ESC's.
while True: 
    calibrateESC(motor1, escSpeedPin)
    time.sleep(0.001)
time.sleep(10)

escSpeed = getAngle(escSpeedPin)
motor1.angle = escSpeed
motor2.angle = escSpeed
