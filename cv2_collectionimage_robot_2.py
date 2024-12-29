from gpiozero import Robot, LED
import cv2
import numpy as np

# ���Ϳ� LED ����
frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))
red_led = LED(17)  # ���� LED (���� ����)
green_led = LED(27)  # �ʷ� LED (���� �� ����)
speed_init = 0.5

def key():
    keyValue = cv2.waitKey(10)
    
    if keyValue == ord('q'):
        return "quit"
    elif keyValue == ord('w'):  # 'w' Ű
        print("go")
        return "go"
    elif keyValue == ord('s'):  # 's' Ű (����)
        print("back")
        return "back"
    elif keyValue == ord('a'):  # 'a' Ű
        print("left")
        return "left"
    elif keyValue == ord('d'):  # 'd' Ű
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
    red_led.on()  # ���� ���¿��� ���� LED �ѱ�
    green_led.off()  # ���� ������ LED ����

def update_speed_based_on_state(carState):
    if carState == "go":
        return 0.8  # ���� �ӵ�
    elif carState in ["left", "right"]:
        return 0.5  # ���� ȸ�� �ӵ�
    elif carState == "back":
        return 0.5  # ���� �ӵ�
    else:
        return 0  # ����

def process_image(image):
    height, _, _ = image.shape
    img = image[int(height / 2):, :, :]  # ���� 1/2 �� ����
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB -> YUV
    img = cv2.GaussianBlur(img, (3, 3), 0)  # �� ó��
    img = cv2.resize(img, (200, 66))  # ũ�� ����
    return img

def save_image(carState, img, filepath, index):
    angle_mapping = {
        "left": 45,
        "right": 135,
        "go": 90,
        "back": 270,  # ���� ����
        "stop": 0
    }
    
    if carState in angle_mapping:
        angle = angle_mapping[carState]
        cv2.imwrite(f"{filepath}_{index:05d}_{angle:03d}.png", img)
        return index + 1  # �ε��� ����
    return index  # ���� ���� ������ �״�� ��ȯ

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # ���� �ػ�
    cam.set(4, 480)  # ���� �ػ�
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
            green_led.on()  # ���� ������ LED �ѱ�
            red_led.off()  # ���� ������ LED ����
        elif action == "back":
            carState = "back"
            speed_init = update_speed_based_on_state(carState)
            back(speed_init)  # ����
            green_led.on()
            red_led.off()
        elif action == "stop":
            carState = "stop"
            speed_init = update_speed_based_on_state(carState)
            stop()
        elif action == "left":
            carState = "left"
            speed_init = update_speed_based_on_state(carState)
            frontwheel.left(speed=0.5)  # �������� ȸ��
            rearwheel.left(speed=0.5)
            green_led.on()
            red_led.off()
        elif action == "right":
            carState = "right"
            speed_init = update_speed_based_on_state(carState)
            frontwheel.right(speed=0.5)  # ���������� ȸ��
            rearwheel.right(speed=0.5)
            green_led.on()
            red_led.off()

        _, image = cam.read()
        img_org = cv2.flip(image, -1)
        cv2.imshow('Original', img_org)

        img_processed = process_image(img_org)
        cv2.imshow('Save', img_processed)

        # �̹��� ���� ó��
        i = save_image(carState, img_processed, filepath, i)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    stop()
