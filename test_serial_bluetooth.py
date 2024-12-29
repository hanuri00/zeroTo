import serial

bt = serial.Serial("/dev/ttyAMA0", baudrate=9600,timeout=1.0)

try:
    while True:
        data = bt.read()
        print(data)
except KeyboardInterrupt:
    print("Keyboard Stopped")
finally:
    bt.close()
