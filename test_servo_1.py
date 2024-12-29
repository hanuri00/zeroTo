from gpiozero import Servo
from time import sleep

servo_1 = Servo(22)

try:
    while True:
        servo_1.min()
        sleep(1)
        servo_1.mid()
        sleep(1)
        servo_1.max()
        sleep(1)
except KeyboardInterrupt:
    print("stop")