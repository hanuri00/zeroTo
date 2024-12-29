from gpiozero import Motor
import cv2
import numpy as np

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

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)                     #가로
    cam.set(4, 480)                     #세로

    while ( cam.ioOpened() ):
        key()

        _, image = cam.read()
        img_org = cv2.flip(image, -1)
        cv2.imshow( 'Original', img_org)

        height, _, _ = img.shape
        img_half = img_org[ int(height/2):,:,:]                  #높이 1/2 만 저장
        img_yuv = cv2.cvtColor(img_half, cv2.COLOR_BRG2YUV)  #RGB -> YUV
        img_blur = cv2.GaussianBlur( img_yuv, (3, 3), 0)    #(3, 3) 픽셀 or (5, 5) 픽셀
        img_resize = cv2.resize(img_blur, (200,66) )        #DNN 활용하기 위해 이미지 보정
        cv2.imshow( 'Save', img_resize)

    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
    stop()    
    
