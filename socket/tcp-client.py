from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = str.encode(input('Please input your messages:'))
clientSocket.send(message)
modifiedMessage = clientSocket.recv(1024)
print(bytes.decode(modifiedMessage))
clientSocket.close()