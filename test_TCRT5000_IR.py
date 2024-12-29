import RPi.GPIO as GPIO

sensor_pin = 11

# GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        sensor_value = GPIO.input(sensor_pin)
        print("value : {}".format(sensor_value))
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
