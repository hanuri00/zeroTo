# -*- condig: uft-8 -*-

from gpiozero import Button
from picamera import PiCamera

btn = Button(2)
cam = PiCamera()
cam.start_preview()
frame = 1

try:
    while True:
        btn.wait_for_press()
        cam.capture('/home/pi/img/frame%03d.jpg' % frame)
        frame += 1
        
except Exception as err:
    예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)

