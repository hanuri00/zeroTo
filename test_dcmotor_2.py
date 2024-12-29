from gpiozero import Motor
from time import sleep

front_wheel_R = Motor(5, 6)
front_wheel_L = Motor(19, 26)

try:
    while True:
        front_wheel_R.forward(speed=0.6)
        front_wheel_L.forward(speed=0.6)
        sleep(3)
        
        front_wheel_R.backward(speed=0.3)
        front_wheel_L.backward(speed=0.3)
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    front_wheel_R.stop()
    front_wheel_L.stop()

