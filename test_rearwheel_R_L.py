from gpiozero import Motor
from time import sleep

rearwheel_R = Motor(5, 6)
rearwheel_L = Motor(19, 26)

try:
    while True:
        rearwheel_R.forward(speed=1)
        rearwheel_L.forward(speed=1)
        sleep(3)
        
        rearwheel_R.backward(speed=0.7)
        rearwheel_L.backward(speed=0.7 )
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    rearwheel_R.stop()
    rearwheel_L.stop()
