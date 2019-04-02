# coding:utf-8
import socket
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录   \hezi.html
HTML_ROOT_DIR = "./html"

WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    def __init__(self, port):
        # 等待客户端的连接
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 拿到server_socket实例,修改一些参数 : 什么级别 (SOCKET级别的) . 设置的socket选项,重用地址 前一个选项值设置为1
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 任意的ip地址
        # self.server_socket.bind(('', port))

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s]用户连接上了" % client_address)

            # handle_client 函数名  args handle_client函数需要的参数
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            # handle_client_process 开启客户端的进程
            handle_client_process.start()
            # 关闭主进程 的 client_socket , 因为这里创建子进程已经复制了一份client_socket,
            client_socket.close()

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s" % header

        self.response_headers = response_headers

    def handle_client(self, client_socket):
        # 双引号内不用加反斜杠
        # 单引号内必须加反斜杠
        # 三单引号输入换行需要加单引号
        # 三双引号最为完美，换行转义什么都不用加

        """"处理客户端请求"""
        # 开启进程的时候 也就意味着 有一个用户 经过了三次握手,客户端可以发送数据过来了 ,进行接收http的报文
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request_data", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print("request_lines", line)
        # 'GET /HTTP/1.1
        # 提取用户请求的文件名
        request_start_line = request_lines[0]
        # file_name = re.match(r"\w+ (/[^ ]* ) ", request_start_line.decode("utf-8")).group(1)
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        method = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

        #      "/aaaaaa.py"
        if file_name.endswith(".py"):
            try:
                # 执行py文件
                m = __import__(file_name[1:-3])
            except Exception:
                self.response_headers = "HTTP1.1 404 NOT FOUND\r\n"
                response_body = "The file is not found!"

            else:
                # 环境变量 env
                env = {
                    "path_info": file_name,
                    "METHOD": method
                }
                response_body = m.application(env, self.start_response)
            response = self.response_headers + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/hezi.html"

            # 打开文件读取内容  b二进制
            try:
                file = open(HTML_ROOT_DIR + file_name, 'rb')

            except IOError:
                # 构造响应数据
                response_start_line = "HTTP1.1 404 NOT FOUND\r\n"
                response_headers = 'Server: My server\r\n'
                response_body = "The file is not found!"
            else:
                file_data = file.read()
                file.close()

                # 构造响应数据
                response_start_line = "HTTP1.1 200 OK\r\n"
                response_headers = 'Server: My server\r\n'
                response_body = file_data.decode("utf-8")

            response = response_start_line + response_headers + "\r\n" + str(response_body)

        print("response", response)
        # 向客户端返回响应数据
        # Python3 的send 必须是字节类型的 ,Python2不需要
        client_socket.send(bytes(response, 'utf-8'))
        # 关闭客户端连接
        client_socket.close()


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8080)
    http_server.start()


# 只有本文件作为启动文件时 ,才会去执行, 被导入到其他文件的时候就不会去执行了
if __name__ == '__main__':
    main()
