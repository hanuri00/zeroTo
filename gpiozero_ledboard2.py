# -*- coding: utf-8 -*-

from gpiozero import LED
from signal import pause
from time import sleep

leds = LEDBoard(5, 6, 13, 19, 26, pwm=True)

try:
	while True:
		leds.value = (0.2, 0.4, 0.6, 0.8, 1.0)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    print("프로그램이 종료되었습니다.")
