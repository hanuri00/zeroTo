# -*- condig: uft-8 -*-

from gpiozero import Motor
from time import sleep

mt = Motor(forward=20, backward=21)

try:
    while True:
        print('모터 회전방향 : Forward')
        mt.forward(speed=0.3)
        sleep(5)

        print('모터 회전방향 : backward')
        mt.backward(speed=0.5)
        sleep(5)
        
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)

