from gpiozero import Motor
import cv2
import numpy as np

leftwheel_front = Motor(25, 16)
leftwheel_back = Motor(20, 21)
rightwheel_front = Motor(5, 6)
rightwheel_back = Motor(19, 26)

def key():
    keyValue = cv2.waitKey(10)
    #print(str(value(KeyValue))
    
    if keyValue == ord( ' q ' ):
        break
    elif keyValue == 82:
        print(" up ")
    elif keyValue == 84:
        print(" down ")
    elif keyValue == 81:
        print(" left ")
    elif keyValue == 83:
        print(" right ") 

def stop():
    leftwheel_front.stop()
    leftwheel_back.stop()
    rightwheel_front.stop()
    rightwheel_back.stop()

def go(speed):
    stop()
    leftwheel_front.forward(speed)
    leftwheel_back.forward(speed)
    rightwheel_front.forward(speed)
    rightwheel_back.forward(speed)

def back(speed):
    stop()
    leftwheel_front.backward(speed)
    leftwheel_back.backward(speed)
    rightwheel_front.backward(speed)
    rightwheel_back.backward(speed)

def right(speed):
    stop()
    rightwheel_front.forward(speed)
    rightwheel_back.forward(speed)

def left(speed):
    stop()
    leftwheel_front.forward(speed)
    leftwheel_back.forward(speed)

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)                     #가로
    cam.set(4, 480)                     #세로

    while ( cam.ioOpened() ):
        key()

        _, img = cam.read()
        img = cv2.flip(img, -1)
        cv2.imshow( 'Original', img)

        height, _, _ = img.shape
        img_org = img[ int(height/2):,:,:]                  #높이 반절
        img_yuv = cv2.cvtColor(img_org, cv2.COLOR_BRG2YUV)  #RGB -> YUV
        img_blur = cv2.GaussianBlur( img_yuv, (3, 3), 0)    #/////////////
        img_resize = 
        cv2.imshow( 'Save', img_save)

    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
    GPIO.cleanup()    
    
