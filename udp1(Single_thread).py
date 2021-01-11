#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
serverip="192.168.0.109"
serverport=307
while True:
    print('''
         ==============
               Window 10
         ==============''')
    data=input("\t")
    data=data.encode()
    print("\tSent!!!!")

    s.sendto(data,(serverip , serverport))
    x=s.recvfrom(256)
    data=x[0].decode()
    print('''\t\t\t\t\t\t\t\t\t\t
         \t\t\t\t\t\t\t\t\t\t============
        \t\t\t\t\t\t\t\t\t\t\tRHEL 8
         \t\t\t\t\t\t\t\t\t\t============''')
    print("\t\t\t\t\t\t\t\t\t\t\t",data)
    print("\t\t\t\t\t\t\t\t\t\t\tReceived!!!!!")


# In[ ]:




