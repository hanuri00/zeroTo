from gpiozero import DistanceSensor, Robot
from time import sleep

def forward(frontwheel, realwheel):
    frontwheel.forward()
    realwheel.forward()

def stop(frontwheel, realwheel):
    frontwheel.stop()
    realwheel.stop()

def control_motor(distance, frontwheel, realwheel):
    if distance > 5:
        print('Forward')
        forward(frontwheel, realwheel)        
    else:
        print('Stop')
        stop(frontwheel, realwheel)

def measure_distance(frontwheel, realwheel):
    ultra = DistanceSensor(trigger=23, echo=24)
    try:
        while True:
            current_distance = ultra.distance * 100  # 거리 값을 cm로 변환
            print(f'Distance : {current_distance:.2f} cm')  # 소수점 두 자리까지 출력
            control_motor(current_distance, frontwheel, realwheel)  # 거리 값으로 모터 제어
            sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by user.")
    finally:
        stop(frontwheel, realwheel)  # 프로그램 종료시 모터 정지

def main():
    frontwheel = Robot(left=(25, 16), right=(20, 21))
    realwheel = Robot(left=(5, 6), right=(19, 26))

    measure_distance(frontwheel, realwheel)

if __name__ == "__main__":
    main()
