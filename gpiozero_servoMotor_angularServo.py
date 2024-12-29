# -*- condig: uft-8 -*-

from gpiozero import AngularServo
from time import sleep

sv = AngularServo(16, min_angle=-90, max_angle=90)

try:
    while True:
        sv.angel=-90
        sleep(2)
        sv.angle=-45
        sleep(2)
        sv.angle=0
        sleep(2)
        sv.angle=45
        sleep(2)
        sv.angle=90
        sleep(2)

    except Exception as err:
        print("예외가 발생했습니다 ({0})".format(err))
    except KeyboardInterrupt:
        print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
