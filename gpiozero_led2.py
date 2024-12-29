from gpiozero import LED
from time import sleep

LED_RED = LED(4)
LED_GREEN = LED(17)

try:
	while True:
		LED_RED.on()
		sleep(0.5)
		LED_RED.off()
		sleep(0.5)
	
		LED_GREEN.on()
		sleep(0.5)
		LED_GREEN.off()
		sleep(0.5)

except KeyboardInterrupt:
	pause()
