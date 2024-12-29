import cv2
import os 
from adafruit_servokit import ServoKit
from jd_opencv_lane_detect import JdOpencvLaneDetect
from jd_car_motor_l9110 import JdCarMotorL9110
import time 


# Servo object 
servo = ServoKit(channels=16)
# OpenCV line detector object
cv_detector = JdOpencvLaneDetect()
# DC motor object 
motor = JdCarMotorL9110()

# Camera object: reading image from camera 
cap = cv2.VideoCapture(0)
# Setting camera resolution as 320x240
cap.set(3, 320)
cap.set(4, 240)

# Find ./data folder for labeling data
try:
    if not os.path.exists('./data'):
        os.makedirs('./data')
except OSError:
    print("failed to make ./data folder")

# Create video codec object. We use 'XVID' format for Raspberry pi.
fourcc =  cv2.VideoWriter_fourcc(*'XVID')
#fourcc =  cv2.VideoWriter_fourcc('M','J','P','G')
# Video write object
video_orig = cv2.VideoWriter('./data/car_video.avi', fourcc, 20.0, (320, 240))
#video_orig = cv2.VideoWriter('./data/car_video_lane.avi', fourcc, 20.0, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Prepare real starting 
for i in range(30):
    ret, img_org = cap.read()
    if ret:
        lanes, img_lane = cv_detector.get_lane(img_org)
        angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
        if img_angle is None:
            print("can't find lane...")
            pass
        else:
            print(angle)
            servo.servo[0].angle = angle + servo_offset			
    else:
        print("camera error")

# Start motor 
motor.motor_move_forward(10)
while True:
    ret, img_org = cap.read()
    if ret:
        cv2.imshow('lane', img_org)
        video_orig.write(img_org)
        lanes, img_lane = cv_detector.get_lane(img_org)

        angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
        if img_angle is None:
            print("angle image out!!")
            pass
        else:
            print(angle)
        servo.servo[0].angle = angle + servo_offset
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("cap error")

if img_angle is None:
    print("angle image out!!")
        pass
else:
    print(angle)
        servo.servo[0].angle = angle + servo_offset

motor.motor_stop()
cap.release()
video_orig.release()
cv2.destroyAllWindows() 
