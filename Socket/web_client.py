import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))
request = """GET / HTTP/1.1\r
Host: 127.0.0.1:5000\r
Cache-Control: max-age=0\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r
Accept-Encoding: gzip, deflate, br\r
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n"""
s.send(request.encode())

buf = s.recv(1024)
while len(buf):
    print(buf)
    buf = s.recv(1024)