import cv2 as cv
import numpy as np
from gpiozero import Robot
from time import sleep

frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))

def key():
    keyValue = cv.waitKey(10)

    if keyValue == 27:          #esc key
        break

def go(speed):
    frontwheel.forward(speed)
    rearwheel.forward(speed)

def back(speed):
    frontwheel.backward(speed)
    rearwheel.backward(speed)

def goleft(speed):
    frontwheel.forward(curve_left=speed)
    rearwheel.forward(curve_left=speed)

def goright(speed):
    frontwheel.forward(curve_right=speed)
    rearwheel.forward(curve_right=speed)

def turnleft(speed):
    frontwheel.left(speed=0.7)
    rearwheel.left(speed=0.7)

def turnright(speed):
    frontwheel.right(speed=0.7)
    rearwheel.right(speed=0.7)

def stop():
    frontwheel.stop()
    rearwheel.stop()

def main():
    cam = cv.VideoCapture(-1)
    cam.set(3, 400)         #너비 400   200
    cam.set(4, 132)         #높이 132   66

 

    while ( cam.isOpened() ):
        key()

        ret, frame = cam.read()
        frame = cv.filp(frame, -1)      # -1은 180도 뒤집음
        cv.imshow('Display', frame)

        img_crop = frame[66:132, 0:200] #세로 66~132, 가로 0~220픽셀로 자름
        img_gray = cv.cvtColor(img_crop, cv.COLOR_BAYER_BG2GRAY)    #이미지를 회색으로
        img_blur = cv.GaussianBlur(img_gray, (5, 5), 0)        #(5,5), (3,3)
        ret, thresh1 = cv.threshold(img_blur, 123, 255, cv.THRESH_BINARY_INV)       #임계점 처리

        #이미지를 압축해서 노이즈를 없앰
        mask = cv.erode(thresh1, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)
        cv.imshow('Dispaly Mask', mask)

        #이미지의 윤곽선을 검출
        contours, hierarchy = cv.findContours(mask.copy(), 1, cv.CHAIN_APPROX_NONE)

        #윤곽선이 있다면 max 반환, 모멘트 계산
        if len(contours) >0:
            c = max(contours, key=cv.contourArea)
            M = cv.moments(c)
        
        #x축과 y축의 무게중심 구한다
        cx = int( M['m10'] / M['m00'])
        cy = int( M['m01'] / M['m00'])

        #x축의 무게중심을 출력한다.
        #cv.line(img_crop, (cx, 0), (cx, 720), (255,0,0), 1)
        #cv.line(img_crop, (cy, 0), (cy, 720), (255,0,0), 1)

        #cv.drawContours(img_crop, contours, -1, (0,255,0),1)
        #print(cx)

        if cx>=95 and cx<=125:
            print("Left")
            goleft(1.0)
        elif cx>=39 and cx<=65:
            print("Right")
            goright(1.0)
        else:
            print("GOGO")
            go(1.0)

    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
    stop()