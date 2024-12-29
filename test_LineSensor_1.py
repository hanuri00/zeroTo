from gpiozero import LineSensor
from time import sleep

line_left_1 = LineSensor(27)
line_left_2 = LineSensor(22)
line_right_1 = LineSensor(17)
line_right_2 = LineSensor(4)

#sensor.when_line = lambda: print('Line detected')
#sensor.when_no_line = lambda: print('No line detected')
try:
    while True:
        print("left 1 : ",line_left_1, "left 2", line_left_2)
        print("right 1 : ",line_right_1, "right 2", line_right_2)
        sleep(1)
        
except KeyboardInterrupt:
    print("Keyboard Stopped")
