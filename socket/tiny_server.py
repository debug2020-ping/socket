from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
try:
    serverSocket.bind(('',6789))
    serverSocket.listen(1)
    while True:
        print('The server is running')
        connectionSocket,addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(4096)
            print(message)
            filename = message.split()[1]
            print(filename)
            f = open(filename[1:],encoding='utf-8')
            outputdata = f.read()
            header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html; charset=utf-8\nContent-Length: %d\n\n' %(len(outputdata))
            connectionSocket.send(header.encode('utf-8'))
            for i in range(0,len(outputdata)):
                connectionSocket.send(str.encode(outputdata[i]))
            connectionSocket.close()
        except IOError:
            header = ' HTTP/1.1 404 Found'
            connectionSocket.send(header.encode())
        finally:
            connectionSocket.close()
finally:
    serverSocket.close()
