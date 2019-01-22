#!/usr/bin/python3

# 导入 socket、sys 模块
import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

res_bytes = b''
while True:
    recv_bytes = s.recv(10)
    msglen = len(recv_bytes)
    if msglen == 0:
        break
    res_bytes = res_bytes + recv_bytes

s.close()

print (res_bytes.decode())