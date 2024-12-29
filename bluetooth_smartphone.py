# -*- condig: uft-8 -*-

from bluetooth import *

server_socket= BluetoothSocket(RFCOMM)

port = 1
server_socket.bind(("", port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

client_socket.send("bluetooth connected!")

try:
    while True:
        data = client_socket.recv(1024)
        print("Received: %s" %data)
        if(data=="q"):
            print("Quit")
            break
except Exception as err:
    예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    client_socket.close()
    server_socket.close()
