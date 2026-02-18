#create a socket
from socket import *

#create a message to send
clientSocket = socket(AF_INET, SOCK_DGRAM)
myMSG = 'Hello'
myMSG = myMSG.encode()

while (myMSG != 'exit'):
    myMSG = "Hello, Server! This is the client."
    myMSG = myMSG.encode()
    myMSG = input('Me: ').encode()


#sent it to the server

clientSocket.sendto(myMSG, ('127.0.0.1', 9090))
# close everything
clientSocket.close()