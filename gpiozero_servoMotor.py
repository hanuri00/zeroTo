# -*- condig: uft-8 -*-

from gpiozero import Servo
from time import sleep

sv = Servo(16)

try:
    while True:
        sv.min()
        sleep(1)
        sv.mid()                #servo.value = 0.5
        sleep(1)
        sv.max()
        sleep(1)

except Exception as err:
    예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)

