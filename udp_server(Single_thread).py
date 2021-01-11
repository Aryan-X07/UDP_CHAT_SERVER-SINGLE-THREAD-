import socket 
import os
import time

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip="192.168.0.109"
port=307
s.bind((ip , port))
while True:
    x=s.recvfrom(256)
    clientip = x[1][0]
    data=x[0].decode()
    print('=============')
    print('  Window 10')
    print('=============')
    print(data)
    print("Recieved!!!!")
    print("\t\t\t\t\t\t=============")
    print('\t\t\t\t\t\t  Rhel 8')
    print('\t\t\t\t\t\t=============')
    data=input("\t\t\t\t\t\t")
    data=data.encode()
    s.sendto(data,(x[1]))
    print("\t\t\t\t\t\tSent!!!!")
