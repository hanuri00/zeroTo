from gpiozero import TonalBuzzer
from time import sleep

bz = TonalBuzzer(12)

try:
    while True:
        bz.play('37')          #C4
        sleep(1)
        bz.play(39)
        sleep(1)
        bz.play(41)
        sleep(1)
        bz.play(42)
        sleep(1)
        bz.play(44)
        sleep(1)
        bz.play(46)
        sleep(1)
        bz.play(48)
        sleep(1)
        bz.play(49)
        sleep(1)
        
except KeyboardInterrupt:
    print("keyboard stop")
finally:
    bz.off()

              




