from gpiozero import DistanceSensor
from time import sleep

ultra = DistanceSensor( trigger=23, echo=24)

try:
    while True:
        print('Distance : ', ultra.distance, 'm')
        sleep(1)
        
except KeyboardInterrupt:
    print("keyboard stop")

              

