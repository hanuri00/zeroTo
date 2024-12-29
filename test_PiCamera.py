from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep

cam = PiCamera()

def cap():
    cam.capture(f'/home/pi/Desktop/AI_Car/img/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')

try:
    while True:
        cap()
        sleep(2)        
        
except KeyboardInterrupt:
    print("keyboard stop")

              

