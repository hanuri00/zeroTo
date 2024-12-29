from gpiozero import Robot
import cv2 as cv

def key():
    keyValue = cv.waitKey(10)
    #print(str(value(KeyValue))
    
    if keyValue == 27:
        break
    elif keyValue == 82:
        print(" ↑ ")
    elif keyValue == 84:
        print(" ↓ ")
    elif keyValue == 81:
        print(" ← ")
    elif keyValue == 83:
        print(" → ")
    elif keyValue == 82 and keyValue == 81:
         print(" ←↑  ")
    elif keyValue == 82 and keyValue == 83:
         print(" ↑→ ")

def main():
    cam = cv.VideoCapture(0)
    cam.set(3, 640)                     #가로
    cam.set(4, 480)                     #세로

    while ( cam.ioOpened() ):
        key()

        ret, image = cam.read()
        img = cv.flip(image, -1)
        cv.imshow( 'Original', img)

    cv.destoryAllWindows()

if __name__ == '__main__':
    main()
    stop()
