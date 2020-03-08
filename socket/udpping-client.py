from socket import *
import time
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0,10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i + 1, sendTime)).encode()
    try:
        clientSocket.sendto(message,('localhost',12001))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        rtt = time.time()-sendTime
        print(rtt)
    except Exception as e:
        print(e)
clientSocket.close()