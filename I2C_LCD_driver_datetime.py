# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

import I2C_LCD_driver
from time import *
from signal import pause

lcd = I2C_LCD_driver.lcd()
lcd.clear()

try:
    while True:
        now=locatltime()
        dt = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
	tt = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)

        lcd.lcd_display_string(dt, 1)
        sleep(0.5)
        lcd.lcd_display_string(tt, 2)
        sleep(1)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
    pause() 
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    lcd.clear()
    print("프로그램이 종료되었습니다.)
    
