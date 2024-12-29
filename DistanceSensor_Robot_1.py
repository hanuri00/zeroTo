from gpiozero import DistanceSensor, Robot
from time import sleep

def forward():
    frontwheel.forward()
    realwheel.forward()

def stop():
    frontwheel.stop()
    realwheel.stop()

def control_motor(distance):
    if distance > 5:
        print('Forward')
        forward()        
    else:
        print('Stop')
        stop()

def distance():
    ultra = DistanceSensor(trigger=23, echo=24)
    try:
        while True:
            current_distance = ultra.distance * 100         # �Ÿ� ���� cm�� ��ȯ
            print(f'Distance : {current_distance:.2f} cm')  # �Ҽ��� �� �ڸ����� ���
            control_motor(current_distance)                 # �Ÿ� ������ ���� ����
            sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user.")
        stop()                  # ���α׷� ����� ���� ����

def main():
    global frontwheel, realwheel
    frontwheel = Robot(left=(25, 16), right=(20, 21))
    realwheel = Robot(left=(5, 6), right=(19, 26))

    distance()

if __name__ == "__main__":
    main()
