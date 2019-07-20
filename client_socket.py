import socket
import sys
import time

#CLIENT

s= socket.socket()
host = input(str("please enter host name:"))

port = 1234

try:
    s.connect((host, port))
    print("connected to server")

except:
    print("connection to server is failed")

while 1:
    # revc byte
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("server:>>", incoming_msg)

    msg = input(str("You:>>"))
    msg = msg.encode()
    s.send(msg)
