#import socket tools
from socket import *

#create a socket object
serverSocket = socket(AF_INET,SOCK_DGRAM)

#specify that I need a specific port
serverSocket.bind( ('172.16.0.4',9090) )

print("The server is ready to receive")
msg = None
#listen for incoming data, and store into a variable
msg, clientAddress = serverSocket.recvfrom(2048)
msg = msg.decode()
#print whatever we get
print(msg)

#close everything
serverSocket.close()