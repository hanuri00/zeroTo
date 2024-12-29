from gpiozero import Motor
from time import sleep

leftwheel_front = Motor(25, 16)
leftwheel_back = Motor(20, 21)
rightwheel_front = Motor(5, 6)
rightwheel_back = Motor(19, 26)

try:
    while True:
        leftwheel_front.forward(speed=1)
        leftwheel_back.forward(speed=1)
        rightwheel_front.forward(speed=1)
        rightwheel_back.forward(speed=1)
        sleep(3)
        
        leftwheel_front.backward(speed=0.7)
        leftwheel_back.backward(speed=0.7 )
        rightwheel_front.backward(speed=0.7)
        rightwheel_back.backward(speed=0.7 )
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    leftwheel_front.stop()
    leftwheel_back.stop()
    rightwheel_front.stop()
    rightwheel_back.stop()
