# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

from gpiozero import LED, Button
from time import sleep


try:

    while True:
        

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
