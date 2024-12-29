# -*- coding: utf-8 -*-

from gpiozero import LED
from signal import pause
from time import sleep

led = LED(17)

try:
	while True:
		led.on()
		sleep(0.5)
		led.off()
		sleep(0.5)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    print("프로그램이 종료되었습니다.")
