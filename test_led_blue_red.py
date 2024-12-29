from gpiozero import LED
from time import sleep

blue_led = LED(20)
red_led = LED(21)

try:
    while True:
        blue_led.on()
        red_led.off()
        sleep(1)
        blue_led.off()
        red_led.on()
        sleep(1)
except KeyboardInterrupt:
    print("keyboard stop")

              