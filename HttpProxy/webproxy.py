import threading
import socket
import time

buf_size = 1024


class ConnThread(threading.Thread):
    def __init__(self, client, addr):
        super().__init__()
        self.client = client  # 浏览器
        self.addr = addr  # 浏览器ip地址
        self.server = None  # 目标服务器

    def run(self):
        src_data, hostname, port, ssl_flag = self.get_data_from_header(self.client)
        dst_data = self.get_data_from_host(hostname, port, src_data, ssl_flag)

        if dst_data and not ssl_flag:
            self.ssl_client_server_client(dst_data)
        elif ssl_flag:
            sample_data_to_client = b"HTTP/1.0 200 Connection Established\r\n\r\n"
            self.ssl_client_server_client(sample_data_to_client)
        else:
            print('pls check network. cannot get hostname:' + hostname)

    @staticmethod
    def get_data_from_header(client):
        """
        解析浏览器请求
        """
        while True:
            try:
                header = client.recv(buf_size)
                src_data = header
            except Exception as e:
                print('获取请求异常：'+str(e))
                raise e
            if header:
                headers = header.split(b'\r\n')
                ssl_flag = headers[0].find(b'CONNECT') > -1
                host_str = headers[1].decode()[6:]
                if ':' in host_str:
                    arr = host_str.split(':')
                    hostname = arr[0]
                    port = int(arr[1])
                else:
                    hostname = host_str
                    port = 80
                break
        return src_data, hostname, port, ssl_flag

    def get_data_from_host(self, hostname, port, src_data, ssl_flag):
        """
        http：与目标服务器建立连接，转发请求，获取返回
        https ：与目标服务器建立连接
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        all_dst_data = ""
        try:
            self.server.connect((str(hostname), port))
        except Exception as e:
            print(e)
            print("get_data_from_host: cannot get host:" + hostname)
            self.server.close()
            return False
        try:
            if ssl_flag:
                return all_dst_data
            else:
                self.server.sendall(src_data)
        except Exception as e:
            print(e)
            print("cannot send data to host:" + hostname)
            self.server.close()
            return False
        rc_data = self.server.recv(buf_size)
        return rc_data

    def ssl_client_server_client(self, dst_data):
        """
        启动两个线程双向收发数据
        """
        try:
            self.client.sendall(dst_data)
        except Exception as e:
            print(e)
            print("cannot sent data(HTTP/1.0 200) to SSL client")
            return False
        threadlist = []
        t1 = threading.Thread(target=self.ssl_client_server)
        t2 = threading.Thread(target=self.ssl_server_client)
        threadlist.append(t1)
        threadlist.append(t2)
        for t in threadlist:
            t.start()
        # 等待与目标服务器断开连接
        while not self.server._closed:
            time.sleep(1)
        self.client.close()

    def ssl_client_server(self):
        while True:
            try:
                ssl_client_data = self.client.recv(buf_size)
            except Exception as e:
                print("client disconnct ")
                print(e)
                self.client.close()
                return False

            if ssl_client_data:
                try:
                    self.server.sendall(ssl_client_data)
                except Exception as e:
                    print("server disconnct Err")
                    self.server.close()
                    return False
            else:
                self.client.close()
                return False

    def ssl_server_client(self):
        while True:
            try:
                ssl_server_data = self.server.recv(buf_size)
            except Exception as e:
                print("server disconnct ")
                self.server.close()
                return False

            if ssl_server_data:
                #####send data to client
                try:
                    self.client.sendall(ssl_server_data)
                except Exception as e:
                    print("Client disconnct Err")
                    self.client.close()
                    return False
            else:
                self.server.close()
                return False


class Server(object):
    def __init__(self, host, port):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind((host,port))
        tcp_server.listen(20)
        self.tcp_sever = tcp_server

    def start(self):
        while True:
            try:
                client, addr = self.tcp_sever.accept()
                ConnThread(client,addr).start()
            except Exception as e:
                print('Error Happen！')
                print(e)


if __name__ == "__main__":
    Server("0.0.0.0", 80).start()
