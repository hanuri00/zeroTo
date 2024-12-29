from gpiozero import TonalBuzzer
from time import sleep

bz = TonalBuzzer(12)

try:
    while True:
        bz.play(261.6)
        sleep(1)
        bz.play(293.6)
        sleep(1)
        bz.play(329.6)
        sleep(1)
        bz.play(349.2)
        sleep(1)
        bz.play(391.9)
        sleep(1)
        bz.play(440.0)
        sleep(1)
        bz.play(493.8)
        sleep(1)
        bz.play(523.2)
        sleep(1)
        
except KeyboardInterrupt:
    print("keyboard stop")
finally:
    bz.off()

              



