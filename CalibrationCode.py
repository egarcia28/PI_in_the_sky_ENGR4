import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn
from adafruit_simplemath import map_range

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP1, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)
potentiometer = AnalogIn(board.GP26_A0)

while True:
    x = map_range(potentiometer.value, 275, 65300, -1, 1)
    print(x)
    time.sleep(.01)
    my_servo.throttle = x
    time.sleep(.01)
