# -*- coding: utf-8 -*-

from gpiozero import Button
from signal import pause
from time import sleep

btn = Button(18)

def hello():
    print("안녕하세요!")

def goodbye():
    print("잘가요!")

try:
    while True:
        btn.when_pressed = hello
        when_released = goodbye

        sleep(1)
        pause()
        
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
