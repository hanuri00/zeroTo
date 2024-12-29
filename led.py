from gpiozero import LED
from time import sleep

ledR1 = LED(12)
ledR2 = LED(13)

try:
    while True:
        ledR1.on()
        sleep(1)
        ledR1.off()
        sleep(0.5)
        
        ledR2.on()
        sleep(1)
        ledR2.off()
        sleep(0.5)
except KeyboardInterrupt:
    print("stop")
finally:
    ledR1.off()
    ledR2.off()
    