from socket import *

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM) # create socket IPv4 & TCP
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # allowing the OS to reuse a recently used socket

serverSocket.bind(('',serverPort)) # use IP address computer & serverPort 8000
serverSocket.listen(1) # listening to connections | 1 - number of connections 

print('Server listening and awaiting instructions')
connectSocket, address = serverSocket.accept() # accept connection

print(f'Connect: {str(address)}')
mes = connectSocket.recv(1024)
print(mes)

command = ''
print('Command sending mode is available. Enter "x" to exit.\n')
while command != 'x': # x = exit
    command = input('>> ')
    connectSocket.send(command.encode())
    mes = connectSocket.recv(1024).decode()
    print(mes)

connectSocket.shutdown(SHUT_RDWR) # shutdown
connectSocket.close()
