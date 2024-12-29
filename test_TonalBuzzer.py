from gpiozero import TonalBuzzer
from time import sleep

bz = TonalBuzzer(12)

try:
    while True:
        bz.play("C4")
        sleep(1)
        bz.play("D4")
        sleep(1)
        bz.play("E4")
        sleep(1)
        bz.play("F4")
        sleep(1)
        bz.play("G4")
        sleep(1)
        bz.play("A4")
        sleep(1)
        bz.play("B4")
        sleep(1)
        bz.play("C5")
        sleep(1)
        
except KeyboardInterrupt:
    print("keyboard stop")
finally:
    bz.off()

              


