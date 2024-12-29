from gpiozero import Motor
from time import sleep

rightwheel_front = Motor(5, 6)
rightwheel_back = Motor(19, 26)

try:
    while True:
        rightwheel_front.forward(speed=1)
        rightwheel_back.forward(speed=1)
        sleep(3)
        
        rightwheel_front.backward(speed=0.7)
        rightwheel_back.backward(speed=0.7 )
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    rightwheel_front.stop()
    rightwheel_back.stop()
