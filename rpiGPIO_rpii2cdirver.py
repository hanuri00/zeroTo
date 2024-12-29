# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

import RPi.GPIO as GPIO
from signal import pause
from rpi_lcd import LCD

addr = 0x27

#GPIO.setmode(GPIO.BCM)
#bus = smbus.MSBus(1)

lcd = RPi_I2C_driver.lcd()


try:
    while True:
        lcd.lcd_display_string("Hello !!", 1)
        lcd.lcd_display_string("Raspberry pi!", 2)
        sleep(1)
        lcd.clear()

    sleep(1)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
    pause() 
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    lcd.cleanup()
    print("프로그램이 종료되었습니다.)
