# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

from gpiozero import PWMLED
from time import sleep
from signal import pause

ledR = PWMLED(4)
ledG = PWMLED(17)

try:

    while True:
        ledR.value = 0          #off
        sleep(1)
        ledR.value = 0.5        #half brightness
        sleep(1)
        ledR.value = 1          #full brightness
        sleep(1)
        
        ledG.pulse()
        sleep(1)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
    pause()
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
