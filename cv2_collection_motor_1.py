from gpiozero import Robot
import cv2
import numpy as np

frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))
speed_init = 0.5

def key():
    keyValue = cv2.waitKey(10)
    
    if keyValue == ord('q'):
        return "quit"
    elif keyValue == 82:  # 'up' key
        print("go")
        return "go"
    elif keyValue == 84:  # 'down' key
        print("stop")
        return "stop"
    elif keyValue == 81:  # 'left' key
        print("left")
        return "left"
    elif keyValue == 83:  # 'right' key
        print("right")
        return "right"
    return None

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

def process_image(image):
    height, _, _ = image.shape
    img = image[int(height / 2):, :, :]  # 높이 1/2 만 저장
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB -> YUV
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 블러 처리
    img = cv2.resize(img, (200, 66))  # 크기 조정
    return img

def save_image(carState, img, filepath, index):
    angle_mapping = {
        "left": 45,
        "right": 135,
        "go": 90
    }
    
    if carState in angle_mapping:
        angle = angle_mapping[carState]
        cv2.imwrite(f"{filepath}_{index:05d}_{angle:03d}.png", img)
        return index + 1  # 인덱스 증가
    return index  # 변경 사항 없으면 그대로 반환

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # 가로 해상도
    cam.set(4, 480)  # 세로 해상도
    filepath = "/home/pi/zeroToAI/video/train"
    i = 0
    carState = "stop"

    while cam.isOpened():
        action = key()
        if action == "quit":
            break
        elif action == "go":
            carState = "go"
            go(speed_init)
        elif action == "stop":
            carState = "stop"
            stop()
        elif action == "left":
            carState = "left"
            turnleft(speed_init)
        elif action == "right":
            carState = "right"
            turnright(speed_init)

        _, image = cam.read()
        img_org = cv2.flip(image, -1)
        cv2.imshow('Original', img_org)

        img_processed = process_image(img_org)
        cv2.imshow('Save', img_processed)

        # 이미지 저장 처리
        i = save_image(carState, img_processed, filepath, i)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    stop()
