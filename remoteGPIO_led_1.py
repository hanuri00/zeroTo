from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.137.162')
led = LED(22, pin_factory=factory)

while True:
    led.off()
    sleep(1)     
    led.on()
    sleep(1)