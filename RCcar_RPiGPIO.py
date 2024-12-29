from bluetooth import *
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
server_socket= BluetoothSocket(RFCOMM)
server_socket.bind(("", PORT_ANY))
server_socket.listen(1)
 
print("waiting")
client_socket, address = server_socket.accept()
print("Accepted connection from ", address)
 
client_socket.send("RC car ready!")
 
STOP  = 0
FORWARD  = 1
BACKWARD = 2
 
CH1 = 0
CH2 = 1
 
OUTPUT = 1
INPUT = 0
 
HIGH = 1
LOW = 0
 
ENA = 13
ENB = 21
 
IN1 = 19
IN2 = 26
IN3 = 16
IN4 = 20
 
 
trig = 14
echo = 15
 
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
 
 
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
 
    pwm = GPIO.PWM(EN, 100) 
 
    pwm.start(0)
    return pwm
 
 
def setMotorContorl(pwm, INA, INB, speed, stat):
 
 
    pwm.ChangeDutyCycle(speed)
    
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
 
 
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
 
 
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)
 
 
def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorContorl(pwmB, IN3, IN4, speed, stat)
 
def allstop():
    setMotor(CH1, 80, STOP)
    setMotor(CH2, 80, STOP)
 
GPIO.setmode(GPIO.BCM)
 
 
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)
 
 
while True:
    data = str(client_socket.recv(1024))
    data = data.replace('b','').replace("'",'').replace(" ",'')
    print("Received:", data)
 
    if data=="q":
        print("Stop")
        allstop()
 
    elif data=="w":
        print("Forward")
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, FORWARD)
        time.sleep(10)
        allstop()
 
    elif data=="s":
        print("Backward")
 
        max_time = time.time() + (5)
 
        while data=="s": 
 
            GPIO.output(trig, False)
            time.sleep(0.05)
 
            GPIO.output(trig, True)
            time.sleep(0.00001)
            GPIO.output(trig, False)
 
            while GPIO.input(echo) == 0:
                pulse_start = time.time()
            while GPIO.input(echo) == 1:
                pulse_end = time.time()
 
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17000
            distance = round(distance, 2)
            print('Distance : ', distance,'cm')
 
 
            if (distance >= 0)&(distance <= 10):
                setMotor(CH1, 80, STOP)
                setMotor(CH2, 80, STOP)
                time.sleep(1)
                if time.time() > max_time:
                    break
            elif distance > 10:
                setMotor(CH1, 80, BACKWARD)
                setMotor(CH2, 80, BACKWARD)
                time.sleep(1)
                allstop()
                if time.time() > max_time:
                    break
            elif distance < 0:
                setMotor(CH1, 80, STOP)
                setMotor(CH2, 80, STOP)
                break
 
    elif data=="a":
        print("Left")
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 0, FORWARD)
        time.sleep(3)
        allstop()
 
    elif data=="d":
        print("Right")
        setMotor(CH1, 0, FORWARD)
        setMotor(CH2, 80, FORWARD)
        time.sleep(3)
        allstop()
 
    else:
        pass
