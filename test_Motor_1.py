from gpiozero import Motor
from time import sleep

dcMotor_R1 = Motor(25, 16)

try:
    while True:
        dcMotor_R1.forward(speed=0.6)
        sleep(5)
        
        dcMotor_R1.backward(speed=0.3)
        sleep(5)

except KeyboardInterrupt:
    print("stop")
finally:
    dcMotor_R1.stop()

