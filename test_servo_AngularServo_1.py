from gpiozero import AngularServo
from time import sleep

def set_servo_angle(angle):
    servo.angle = angle

def main():
    global servo
    servo = AngularServo(17, min_angle=-90, max_angle=90)

    angles = [-90, -45, 0, 45, 90]

    try:
        while True:
            for angle in angles:
                set_servo_angle(angle)
                sleep(1)
    except KeyboardInterrupt:
        print("stop")

if __name__ == "__main__":
    main()
