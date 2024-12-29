from gpiozero import Robot, LED
import cv2
import numpy as np

# 모터와 LED 설정
frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))
red_led = LED(17)  # 빨간 LED (정지 상태)
green_led = LED(27)  # 초록 LED (주행 중 상태)
speed_init = 0.5

def key():
    keyValue = cv2.waitKey(10)
    
    if keyValue == ord('q'):
        return "quit"
    elif keyValue == ord('w'):  # 'w' 키
        print("go")
        return "go"
    elif keyValue == ord('s'):  # 's' 키 (후진)
        print("back")
        return "back"
    elif keyValue == ord('a'):  # 'a' 키
        print("left")
        return "left"
    elif keyValue == ord('d'):  # 'd' 키
        print("right")
        return "right"
    return None

def go(speed):
    frontwheel.forward(speed)
    rearwheel.forward(speed)

def back(speed):
    frontwheel.backward(speed)
    rearwheel.backward(speed)

def stop():
    frontwheel.stop()
    rearwheel.stop()
    red_led.on()  # 정지 상태에서 빨간 LED 켜기
    green_led.off()  # 주행 상태의 LED 끄기

def update_speed_based_on_state(carState):
    if carState == "go":
        return 0.8  # 빠른 속도
    elif carState in ["left", "right"]:
        return 0.5  # 느린 회전 속도
    elif carState == "back":
        return 0.5  # 후진 속도
    else:
        return 0  # 정지

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
        "go": 90,
        "back": 270,  # 후진 각도
        "stop": 0
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
            speed_init = update_speed_based_on_state(carState)
            go(speed_init)
            green_led.on()  # 주행 상태의 LED 켜기
            red_led.off()  # 정지 상태의 LED 끄기
        elif action == "back":
            carState = "back"
            speed_init = update_speed_based_on_state(carState)
            back(speed_init)  # 후진
            green_led.on()
            red_led.off()
        elif action == "stop":
            carState = "stop"
            speed_init = update_speed_based_on_state(carState)
            stop()
        elif action == "left":
            carState = "left"
            speed_init = update_speed_based_on_state(carState)
            frontwheel.left(speed=0.5)  # 왼쪽으로 회전
            rearwheel.left(speed=0.5)
            green_led.on()
            red_led.off()
        elif action == "right":
            carState = "right"
            speed_init = update_speed_based_on_state(carState)
            frontwheel.right(speed=0.5)  # 오른쪽으로 회전
            rearwheel.right(speed=0.5)
            green_led.on()
            red_led.off()

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
