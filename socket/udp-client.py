from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = str.encode(input('Please input your messages:'))
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(bytes.decode(modifiedMessage))
print(serverAddress)
clientSocket.close()

