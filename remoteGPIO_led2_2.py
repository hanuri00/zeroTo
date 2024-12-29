from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.137.162')

ledR = LED(17, pin_factory=factory)
ledY = LED(18, pin_factory=factory)

try:
    while True:
        ledR.on()
        sleep(1)
        ledR.off()
        sleep(0.5)

        ledY.on()
        sleep(1)
        ledY.off()
        sleep(0.5)

except ConnectionRefusedError:
    print("Error: Could not connect to pigpio daemon on the remote host.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ledR.close()
    ledY.close()
    print("program end")
