from gpiozero import Robot
import cv2
import numpy as np

frontwheel = Robot(left=(25, 16), right=(20, 21))
rearwheel = Robot(left=(5, 6), right=(19, 26))

speed_init = 0.5

def key():
    keyValue = cv2.waitKey(10)
    #print(str(value(KeyValue))
    
    if keyValue == ord( ' q ' ):
        break
    elif keyValue == 82:
        print(" ↑ ")
        carState = "forward"
        go(speed_init)
    elif keyValue == 84:
        print(" ↓ ")
        carState = "stop"
        stop()
    elif keyValue == 81:
        print(" ← ")
        carState = "left"
        turn_left(speed_init)
    elif keyValue == 83:
        print(" → ")
        carState = "right"
        turn_right(speed_init)
    elif keyValue == 82 and keyValue == 81:
         print(" ←↑  ")
         carState="forward_left"
         forward_left(speed_init)
    elif keyValue == 82 and keyValue == 83:
         print(" ↑→  ")
         carState="forward_right"
         forward_right(speed_init)

def forward(speed):
	frontwheel.forward(speed)
	rearwheel.forward(speed)

def backward(speed):
	frontwheel.backward(speed)
	rearwheel.backward(speed)

def forward_left(speed):				
	frontwheel.forward(speed*0.7, curve_left=speed*0.7)
	rearwheel.forward(speed*0.7, curve_left=speed*0.7)

def forward_right(speed):				
	frontwheel.forward(speed*0.7, curve_right=speed*0.7)
	rearwheel.forward(speed*0.7, curve_right=speed*0.7)

def turn_left(speed):
	frontwheel.left(speed)
	rearwheel.left(speed)

def turn_right(speed):
	frontwheel.right(speed)
	rearwheel.right(speed)

def stop():
	frontwheel.stop()
	rearwheel.stop()


def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)                     #가로
    cam.set(4, 480)                     #세로
    filepath = "/home/pi/zeroToAI/video/train"
    i = 0
    carState = "stop"

    while ( cam.ioOpened() ):
        key()

        _, image = cam.read()
        img_org = cv2.flip(image, -1)
        cv2.imshow( 'Original', img_org)

        height, _, _ = image.shape
        
        #변환 파일(half, yuv, blur, resize) 모두 저장시 아래 코드 실행
        #img_half = img_org[ int(height/2):,:,:]                  #높이 1/2 만 저장
        #img_yuv = cv2.cvtColor(img_half, cv2.COLOR_BRG2YUV)  #RGB -> YUV
        #img_blur = cv2.GaussianBlur( img_yuv, (3, 3), 0)    #(3, 3) 픽셀 or (5, 5) 픽셀
        #img_resize = cv2.resize(img_blur, (200,66) )        #DNN 활용하기 위해 이미지 보정
        #cv2.imshow( 'Save', img_resize)

        #변환파일들을 저장시 속도가 매우 느려지고 용량 부족시 1개 img 파일로만 저장
        img = img_org[ int(height/2):,:,:]                  #높이 1/2 만 저장
        img = cv2.cvtColor(img, cv2.COLOR_BRG2YUV)  #RGB -> YUV
        img = cv2.GaussianBlur( img, (3, 3), 0)    #(3, 3) 픽셀 or (5, 5) 픽셀
        img = cv2.resize(img, (200,66) )        #DNN 활용하기 위해 이미지 보정
        cv2.imshow( 'Save', img)

        if carState == "left":
            #왼쪽 45, 차후 각도 값을 자동을 처리하도록 할 필요있음.
            cv2.imwrite( "%s_%05_%03d.png" * (filepath, i, 45), img )
            i+=1
        elif carState == "right":
            #오른쪽 135, 차후 각도 값을 자동을 처리하도록 할 필요있음.
            cv2.imwrite( "%s_%05_%03d.png" * (filepath, i, 135), img )
            i+=1
        elif carState == "go":
            #중앙 90, 차후 각도 값을 자동을 처리하도록 할 필요있음.
            cv2.imwrite( "%s_%05_%03d.png" * (filepath, i, 90), img )
            i+=1            

    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
    stop()    
    
