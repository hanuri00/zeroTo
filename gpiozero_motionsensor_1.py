# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

from gpiozero import MotionSensor, LED
from signal import pause

sensorNum = 4
ledNum = 16

sensor = MotionSensor(sensorNum)
led = LED(ledNum)

try:
    while True:
        sensor.when_motion = len.on
        sensor.when_no_motion = led.off
        sleep(1)

except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
    pause() 
except KeyboardInterrupt:
    print("키보드 중단")
    pause()
finally:
    print("프로그램이 종료되었습니다.)
    
