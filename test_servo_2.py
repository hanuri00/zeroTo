from gpiozero import AngularServo
from time import sleep

def servo_maxleft():
    servo.angle=-90

def servo_midleft():
    servo.angle=-45

def servo_mid():
    servo.angle=0

def servo_midright():
    servo.angle=45

def servo_maxright():
    servo.angle=90


def main():
    global servo
    servo = AngularServo(17, min_angle=-90, max_angle=90)

    try:
        while True:
            servo_mid()
            sleep(1)
            servo_midleft()
            sleep(1)
            servo_maxleft()
            sleep(1)
            servo_mid()
            sleep(1)
            servo_midright()
            sleep(1)
            servo_maxright()
            sleep(1)
                   
    except KeyboardInterrupt:
        print("stop")

if __name__ == "__main__":
    main()
