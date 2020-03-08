def receiveFromServer():
    msg = clientSocket.recv(1024)
    print(msg)
    return msg


from socket import *
msg = "What to eat tonight?\r\n"
endmsg = "\r\n.\r\n"
mailServer = 'smtp.qq.com'
clientSocket = socket(AF_INET, SOCK_STREAM) # The socket for TCP Connection
clientSocket.connect((mailServer, 587))
recv = receiveFromServer()
if(bytes.decode(recv[:3]) != '220'):
    print ('220 reply not received from server.')
heloCommand = 'EHLO 1498307751\r\n'
clientSocket.sendall(str.encode(heloCommand))
recv1 = receiveFromServer()
if(bytes.decode(recv1[:3]) != '250'):
    print ('250 reply not received from server.')
# Next,we need to login the server
clientSocket.sendall(b'auth login\r\n')
receiveFromServer()
clientSocket.sendall(b'MTQ5ODMwNzc1MQ==\r\n')
receiveFromServer()
clientSocket.sendall(b'U2luZm9yMjAxNA==\r\n')#The base64 code of your password
receiveFromServer()
# Send mail from command
clientSocket.sendall(b'mail from: <1498307751@qq.com>\r\n')
receiveFromServer()
clientSocket.sendall(b'rcpt to: <1498307751@qq.com>\r\n')
receiveFromServer()
clientSocket.sendall(b'data\r\n')
clientSocket.recv(1024)
clientSocket.sendall(b'from:1498307751@qq.com\r\n')
clientSocket.sendall(b'to:1498307751@qq.com\r\n')
clientSocket.sendall(b'subject:kuku is smart\r\n')
clientSocket.sendall(b'Content-Type:text/plain\t\n')#WTF?
clientSocket.sendall(b'\r\n')
clientSocket.sendall(str.encode(msg))
clientSocket.sendall(str.encode(endmsg))
receiveFromServer()
clientSocket.sendall(b'quit\r\n')
receiveFromServer()