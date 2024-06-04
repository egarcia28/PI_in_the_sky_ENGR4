import time                                   #importation  of libraries
import board
import pwmio
import adafruit_mpu6050
import busio         
from adafruit_motor import servo
from analogio import AnalogIn
from adafruit_simplemath import map_range

maxpower = 1                                #constant throttle and timing variables for motor loop
spinuptime = 5
cruisetime = 5
runawaytime = 10

sda_pin = board.GP4                           #defines pin 14 and 15 as SDA and SCL pins
scl_pin = board.GP5                           #needs to be pins 14 and 15 because they are in the sam I2C bus
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)           #initializes the sensor

t = 0                                         #initializes variables for time,x,y,and x accel.
X = 0
Y = 0
X = 0

pwm = pwmio.PWMOut(board.GP1, frequency=50)   # create a PWMOut object on Pin GP1

my_servo = servo.ContinuousServo(pwm)         #initializing motor(servo syntax) and potentiometer
potentiometer = AnalogIn(board.GP26_A0)

starttime = time.monotonic()
my_servo.throttle = -1
print("run.")
time.sleep(runawaytime)

with open("/data.csv", "a") as datalog:                       
    for x in range(-100,100,1):
        datalog.write(f"{time.monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]}\n")
        time.sleep(spinuptime/200)
        print(map_range(x, -100, 100, -1, maxpower))
        my_servo.throttle = map_range(x, -100, 100, -1, maxpower)
        datalog.flush()
    print("zoom")
    while (time.monotonic-starttime) < (spinuptime + cruisetime + runawaytime):
        datalog.write(f"{time.monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]}\n")
        datalog.flush()
        time.sleep(spinuptime/200)
    my_servo.throttle = -1
    print("done.")

        
