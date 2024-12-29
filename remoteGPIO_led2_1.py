from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.137.162')
ledR = LED(17, pin_factory=factory)
ledY = LED(18, pin_factory=factory)

while True:
    ledR.on()
    ledY.off()
    sleep(1)     
    ledR.off()
    ledY.on()
    sleep(1)
