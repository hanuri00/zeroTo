from gpiozero import Buzzer
from time import sleep

bz = Buzzer(12)

try:
    while True:
        bz.beep()      # same bz.toggle()
        sleep(1)
        
except KeyboardInterrupt:
    print("keyboard stop")
finally:
    bz.off()

              

