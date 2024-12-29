from gpiozero import Robot, Motor
from time import sleep

car_R = Robot(left=(25, 16), right=(20, 21))
car_L = Robot(left=(5, 6), right=(19, 26))

try:
    while True:
        car_R.forward()
        car_L.forward()
        sleep(3)
        car_R.backward()
        car_L.backward()
        sleep(3)
        
except KeyboardInterrupt:
    print("stop")
finally:
    car_R.stop()
    car_L.stop()