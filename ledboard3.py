# -*- coding: utf-8 -*-

from gpiozero import LED
from signal import pause
from time import sleep

leds = LEDBoard(2, 3, 4, 5, 6, 7, 8, 9)

try:
	while True:
                for led in leds
                        led.on()
                sleep(1)
                leds.off()

                for led in leds[::2]            #짝수번호 LED on
                        led.on()
                sleep(1)
                leds.off()

                for led in leds[1::2]           #홀수번호 LED on
                        led.on()
                sleep(1)
                leds.off()
                
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    print("프로그램이 종료되었습니다.")
