import cv2
import RPi.GPIO as GPIO
from time import sleep

def main():
    cam = cv2.VideoCapture(-1)
    cam.set(3, 640)
    cam.set(4, 480)

    while ( cam.ioOpened() ):
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

        _, img = cam.read()
        img = cv2.flip(img, -1)
        cv2.imshow( 'Original', img)

        height, _, _ = img.shape
        img_org = img[ int(height/2):,:,:]
        img_yuv = cv2.cvtColor(img_org, cv2.COLOR_BGR2YUV)
        img_blur = cv2.GaussianBlur( img_yuv, (3, 3), 0)
        img_resize = 
        cv2.imshow( 'Save', img_save)

    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
    GPIO.cleanup()    
    
