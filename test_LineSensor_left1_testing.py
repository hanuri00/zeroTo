from gpiozero import LineSensor
from time import sleep

line_left_1 = LineSensor(27, active_state=True)


#sensor.when_line = lambda: print('Line detected')
#sensor.when_no_line = lambda: print('No line detected')
try:
    while True:
        print(line_left_1.is_active)
        print("left 1 : ", line_left_1)
        sleep(1)
        
except KeyboardInterrupt:
    print("Keyboard Stopped")

