from socket import *

tcpSerSock = socket(AF_INET, SOCK_STREAM)# The Server welcome socket
tcpSerSock.bind(('', 8080))#bind it to port number 8080
tcpSerSock.listen(1)

while True:
    print('ready to serve...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('received a connection from:', addr)
    message = tcpCliSock.recv(4096)
    print('The message received from host is as below:')
    print(bytes.decode(message))

    filename = message.split()[1].partition("/")
    print('the file name is : ' + filename)
    fileExist = "false"
    filetouse = "/" + filename
    print('the filetouse is: ' + filetouse)
    try:
        f = open(filetouse[1:],'r')
        outputdata = f.readlines()
        fileExist = 'true'
        for i in range(len(outputdata)):
            tcpCliSock.send(outputdata[i])
        print('read from cache')
    except IOError:
        if(fileExist == 'false'):
            c = socket(AF_INET,SOCK_STREAM)
            serverName = filename.partition('/')[0]
            try:
                c.connect((serverName, 80))
                c.send(message)
                buf = c.recv(4096)
                tmpFile = open("./" + filename, "wb")
                for i in range(0, len(buf)):
                    tmpFile.write(buf[i])
                    tcpCliSock.send(buf[i])
                c.close()
                tmpFile.close()
            except:
                print('Illegal request')
                c.close()
        else:
            print('I do not know what happened now but something bad must happened')
    tcpCliSock.close()
tcpSerSock.close()





