# -*- coding: utf-8 -*-

from time import sleep
from pigpio

pi = pigpio.pi()        # Connect to local Pi.

try:
    while 1:
        pi.set_servo_pulsewidth(18, 1000)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(18, 1500)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(18, 2000)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(18, 1500)
        time.sleep(0.5)
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    # switch servo off
    pi.set_servo_pulsewidth(18, 0);
    pi.stop()
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)
