from gpiozero import LED
from time import sleep

ledR1 = LED(12)
ledR2 = LED(13)

try:
    while True:
        ledR1.blink()
        ledR1.blink()
        #ledR2.blink()
        sleep(1)

except KeyboardInterrupt:
    print("stop")
finally:
    ledR1.off()
    ledR2.off()