'''
�ۼ��� : hanuri
�ڵ� ������ : 2024.12.06
���� : yolo8���� �н������� ������ ��������
'''


from gpiozero import Robot, LED
import cv2
import numpy as np
from ultralytics import YOLO

# ���Ϳ� LED ����
frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))
red_led = LED(17)  # ���� LED (���� ����)
green_led = LED(27)  # �ʷ� LED (���� �� ����)

# YOLOv8 �� �ε�
model = YOLO('/path/to/save/yolov8_lane.pt')

def process_frame(frame):
    results = model(frame)  # �������� �𵨿� ����
    return results

def control_vehicle(lane_position):
    # ���� ��ġ�� ���� ���� ����
    if lane_position < 0.4:
        # �������� ȸ��
        frontwheel.left(0.5)
        rearwheel.left(0.5)
    elif lane_position > 0.6:
        # ���������� ȸ��
        frontwheel.right(0.5)
        rearwheel.right(0.5)
    else:
        # ����
        frontwheel.forward(0.5)
        rearwheel.forward(0.5)

def main():
    cam = cv2.VideoCapture(0)

    while cam.isOpened():
        _, frame = cam.read()
        img_org = cv2.flip(frame, -1)

        # �̹��� ó��
        results = process_frame(img_org)
        lane_position = None  # ���� ��ġ �ʱ�ȭ

        # ��� ó��
        for result in results:
            boxes = result.boxes.xyxy  # �ٿ�� �ڽ�
            if len(boxes) > 0:
                # ���� ù ��° ���� �ڽ��� �߾� ��ġ ���
                x1, y1, x2, y2 = boxes[0]
                lane_position = (x1 + x2) / (2 * img_org.shape[1])  # ������ ��ȯ
                cv2.rectangle(img_org, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        if lane_position is not None:
            control_vehicle(lane_position)

        cv2.imshow('Lane Detection', img_org)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
