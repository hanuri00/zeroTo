import cv2
import numpy as np

def key():
    keyValue = cv2.waitKey(10)

    if keyValue == ord('q'):
        return False
    elif keyValue == 82:
        print("up")
    elif keyValue == 84:
        print("down")
    elif keyValue == 81:
        print("left")
    elif keyValue == 83:
        print("right")
    
    return True

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # 가로
    cam.set(4, 480)  # 세로
    filepath = "/home/pi/zeroToAI/video/train"
    i = 0
    carState = "stop"

    running = True
    while running and cam.isOpened():
        running = key()

        _, image = cam.read()
        img_org = cv2.flip(image, -1)
        cv2.imshow('Original', img_org)

        height, _, _ = image.shape
        
        img = img_org[int(height/2):,:,:]  # 높이 1/2 만 저장
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB -> YUV
        img = cv2.GaussianBlur(img, (3, 3), 0)  # (3, 3) 픽셀 or (5, 5) 픽셀
        img = cv2.resize(img, (200, 66))  # DNN 활용하기 위해 이미지 보정
        cv2.imshow('Save', img)

        if carState == "left":
            cv2.imwrite(f"{filepath}_{i:05d}_045.png", img)
            i += 1
        elif carState == "right":
            cv2.imwrite(f"{filepath}_{i:05d}_135.png", img)
            i += 1
        elif carState == "go":
            cv2.imwrite(f"{filepath}_{i:05d}_090.png", img)
            i += 1            

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
