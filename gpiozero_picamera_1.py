# -*- condig: uft-8 -*-

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

btn = Button(2)
cam = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
    cam.capture('/home/pi/img/%s.jpg' % timestampe)

try:
    while True:
        btn.when_pressed = capture
        
except Exception as err:
    예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)

