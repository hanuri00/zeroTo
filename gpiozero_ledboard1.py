# -*- coding: utf-8 -*-

from gpiozero import LED
from signal import pause
from time import sleep

leds = LEDBoard(5, 6, 13, 19, 26)

try:
	while True:
		leds.on()
		sleep(1)
		leds.off()
		sleep(1)
		leds.value = (1, 0, 1, 0, 1)
		sleep(1)
		leds.blink()

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    print("프로그램이 종료되었습니다.")
