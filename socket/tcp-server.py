from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is running!')
while True:
    connectionSocket,addr = serverSocket.accept()
    print(addr)
    message = connectionSocket.recv(1024)
    modifiedmessage = message.upper()
    connectionSocket.send(modifiedmessage)
    connectionSocket.close()