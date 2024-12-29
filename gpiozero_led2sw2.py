# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

from gpiozero import LED, Button
from time import sleep

ledR = LED(4)
ledG = LED(17)

btnR = Button(6)
btnG = Button(12)

try:

    while True:
        ledR.source = btnR
        sleep(0.5)
        ledG.source = btnG
        sleep(0.5)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
