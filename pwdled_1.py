from gpiozero import PWMLED
from time import sleep

ledR1 = PWMLED(12)
ledR2 = PWMLED(13)


try:
    while True:
        ledR1.value=0.0
        ledR2.value=0.0
        for i in range(10):    
            ledR1.value = ledR1.value + 0.1
            ledR2.value = ledR2.value + 0.1
            sleep(0.3)
except KeyboardInterrupt:
    print("stop")
finally:
    ledR1.off()
    ledR2.off()
    
