from ultralytics import YOLO
import cv2

# YOLOv8 �� �ε�
model = YOLO('path/to/your/model.pt')

# ī�޶� ����
cap = cv2.VideoCapture(0)  # 0�� �⺻ ī�޶� �ǹ���

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # �����ӿ� ���� ��ü Ž�� ����
    results = model.predict(frame)

    # ��� �ð�ȭ
    annotated_frame = results[0].plot()

    # ������ ���
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    # 'q' Ű�� ������ ����
    if cv2.waitKey(1) == ord('q'):
        break

# �ڿ� ����
cap.release()
cv2.destroyAllWindows()