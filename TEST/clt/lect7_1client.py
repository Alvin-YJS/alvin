# client
"""
import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)
"""

"""
#1 서버에 접속하기 위한 소켓을 생성한다.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 서버에 접속을 시도한다.
clientSocket.connect(ADDR)
print('connect is success')
"""

# 채팅 프로그램 (client)
"""
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))
    response = "/0"
    
clientSocket.close()
"""

# ucit.py
"""
import socket

HOST = "127.0.0.1"
PORT = 1234

ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("msg : ")

    sock.sendto(msg.encode('utf-8'), ADDR)
    rsp, srv = sock.recvfrom(1024)
    print("msg : ", rsp)
    rsp = "\0"

sock.close()
"""