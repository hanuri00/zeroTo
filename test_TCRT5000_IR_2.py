import RPi.GPIO as GPIO

TrackingPin = 11

def setup():
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(TrackingPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
 while True:
  if GPIO.input(TrackingPin) == GPIO.LOW:
   # Detectie wit oppervalk (of voorwerp bij sensor)
   print(GPIO.input(TrackingPin))

  else:
   # detectie zwart oppervlak (of geen voorwerp bij sensor)
   #print('zwart')
   print(GPIO.input(TrackingPin))

def destroy():
 GPIO.cleanup()

if __name__ == '__main__':
 setup()
try:
 loop()
except KeyboardInterrupt:
 destroy()