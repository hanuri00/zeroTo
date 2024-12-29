## RPi.GPIO Library
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm=GPIO.PWM(18, 50)
pwm.start(0)
try:
    while 1:
        pwm.ChangeDutyCycle(0)
        sleep(1)
        pwm.ChangeDutyCycle(2.5)
        sleep(1)
        pwm.ChangeDutyCycle(5)
        sleep(1)
        pwm.ChangeDutyCycle(7.5)
        sleep(1)
        pwm.ChangeDutyCycle(10)
        sleep(1)
        pwm.ChangeDutyCycle(15)
        sleep(1)
except KeyboardInterrupt:
    print("exit")
    pwm.stop()
    GPIO.cleanup()
