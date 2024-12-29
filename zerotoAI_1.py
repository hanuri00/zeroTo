'''
작성자 : hanuri
코드 수정일 : 2024.12.06
내용 : yolo8에서 학습데이터 가져와 자율주행
'''


from gpiozero import Robot, LED
import cv2
import numpy as np
from ultralytics import YOLO

# 모터와 LED 설정
frontwheel = Robot(left=(5, 6), right=(25, 16))
rearwheel = Robot(left=(19, 16), right=(20, 21))
red_led = LED(17)  # 빨간 LED (정지 상태)
green_led = LED(27)  # 초록 LED (주행 중 상태)

# YOLOv8 모델 로드
model = YOLO('/path/to/save/yolov8_lane.pt')

def process_frame(frame):
    results = model(frame)  # 프레임을 모델에 전달
    return results

def control_vehicle(lane_position):
    # 차선 위치에 따라 차량 제어
    if lane_position < 0.4:
        # 왼쪽으로 회전
        frontwheel.left(0.5)
        rearwheel.left(0.5)
    elif lane_position > 0.6:
        # 오른쪽으로 회전
        frontwheel.right(0.5)
        rearwheel.right(0.5)
    else:
        # 직진
        frontwheel.forward(0.5)
        rearwheel.forward(0.5)

def main():
    cam = cv2.VideoCapture(0)

    while cam.isOpened():
        _, frame = cam.read()
        img_org = cv2.flip(frame, -1)

        # 이미지 처리
        results = process_frame(img_org)
        lane_position = None  # 차선 위치 초기화

        # 결과 처리
        for result in results:
            boxes = result.boxes.xyxy  # 바운딩 박스
            if len(boxes) > 0:
                # 가장 첫 번째 차선 박스의 중앙 위치 계산
                x1, y1, x2, y2 = boxes[0]
                lane_position = (x1 + x2) / (2 * img_org.shape[1])  # 비율로 변환
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
