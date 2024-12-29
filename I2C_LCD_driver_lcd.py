# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

import I2C_LCD_driver
from time import sleep
from signal import pause

lcd = I2C_LCD_driver.lcd()

try:
    while True:
        lcd.lcd_display_string("Hello !!", 1)
        sleep(0.3)
        lcd.lcd_display_string("Raspberry pi!", 2)

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
    
