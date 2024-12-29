from gpiozero import Motor
from time import sleep

dcMotor_R1 = Motor(25, 16)
dcMotor_R2 = Motor(20, 21)

try:
    while True:
        dcMotor_R1.forward(speed=0.6)
        dcMotor_R2.forward(speed=0.6)
        sleep(3)
        
        dcMotor_R1.backward(speed=0.3)
        dcMotor_R2.backward(speed=0.3)
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    dcMotor_R1.stop()
    dcMotor_R2.stop()
