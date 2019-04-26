import socket

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 5001

server_socket.bind(('127.0.0.1', port))

server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    response = '''HTTP/1.1 200 OK\r
Content-Type: text/html; charset=utf-8\r
Content-Length: 11\r
Date: Tue, 22 Jan 2019 03:15:07 GMT\r
\r
Hello World\r\n'''
    client_connection.sendall(response.encode())
    client_connection.close()
