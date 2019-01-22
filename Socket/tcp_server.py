
import socket

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(1)

while True:
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))
    data = 'Hello! Client!连接地址'
    clientsocket.sendall(data.encode('utf-8'))
    clientsocket.close()
