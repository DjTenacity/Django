# coding:utf-8
import socket
from multiprocessing import Process


def handle_client(client_socket):
    # 双引号内不用加反斜杠
    # 单引号内必须加反斜杠
    # 三单引号输入换行需要加单引号
    # 三双引号最为完美，换行转义什么都不用加

    """"处理客户端请求"""
    # 开启进程的时候 也就意味着 有一个用户 经过了三次握手,客户端可以发送数据过来了 ,进行接收http的报文
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request_data", request_data)

    # 构造响应数据
    response_start_line = "HTTP1.1 200 OK\r\n"
    response_headers = 'Server: My server\r\n'
    response_body = 'hello DJ'

    response = response_start_line + response_headers + "\r\n" + response_body
    print("response", response)
    # 向客户端返回响应数据
    # Python3 的send 必须是字节类型的
    client_socket.send(bytes(response, 'utf-8'))
    # 关闭客户端连接
    client_socket.close()
    pass


# 只有本文件作为启动文件时 ,才回去执行, 被导入到其他文件的时候就不会去执行了
if __name__ == '__main__':
    # 等待客户端的连接
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # // 任意的ip地址
    server_socket.bind(('', 8080))
    # 监听 队列128
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        # print("[s%] [s%]用户连接上了" % client_address)

        # handle_client 函数名  args handle_client函数需要的参数
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        # handle_client_process 开启客户端的进程
        handle_client_process.start()
        # 关闭主进程 的 client_socket , 因为这里创建子进程已经复制了一份client_socket,
        client_socket.close()
