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
            current_distance = ultra.distance * 100         # 거리 값을 cm로 변환
            print(f'Distance : {current_distance:.2f} cm')  # 소수점 두 자리까지 출력
            control_motor(current_distance)                 # 거리 값으로 모터 제어
            sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user.")
        stop()                  # 프로그램 종료시 모터 정지

def main():
    global frontwheel, realwheel
    frontwheel = Robot(left=(25, 16), right=(20, 21))
    realwheel = Robot(left=(5, 6), right=(19, 26))

    distance()

if __name__ == "__main__":
    main()
