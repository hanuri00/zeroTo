from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    factory = PiGPIOFactory(host='192.168.137.162')
    led = LED(22, pin_factory=factory)

    while True:
        led.off()
        sleep(1)
        led.on()
        sleep(1)

except ConnectionRefusedError:
    print("Error: Could not connect to pigpio daemon on the remote host.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("program end")
