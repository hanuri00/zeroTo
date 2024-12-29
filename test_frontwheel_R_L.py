from gpiozero import Motor
from time import sleep

frontwheel_R = Motor(25, 16)
frontwheel_L = Motor(20, 21)

try:
    while True:
        frontwheel_R.forward(speed=1)
        frontwheel_L.forward(speed=1)
        sleep(3)
        
        frontwheel_R.backward(speed=0.7)
        frontwheel_L.backward(speed=0.7 )
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    frontwheel_R.stop()
    frontwheel_L.stop()