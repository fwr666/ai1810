# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# conding=utf-8
'''
HTTP Server v2.0
多线程并发
可以做request解析
能够返回简单的数据
使用类进行封装
'''

from socket import *
from threading import Thread
import sys

# httpserver主体功能


class HTTPServer(object):
     # 客户自己决定的参数，分别是服务器地址，端口，

    def __init__(self, addr, static_dir):
        self.server_address = addr
        self.static_dir = static_dir
        self.ip = addr[0]
        self.port = addr[1]
        # 创建套接字
        self.create_socket()

    # 创建套接子
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(
            SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(self.server_address)

    # 函数功能：监听客户端，为每个客户端连接时创建一个线程，
    # 转到handle执行客户端请求
    def serve_forever(self):  # 服务器套接字
        self.sockfd.listen(3)  # 监听
        print("Listen to the port %d" % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error", e)
                continue

            # 创建线程处理客户端请求
            clientThread = Thread(target=self.handle,
                                  args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    # 处理客户端请求
    # 接收客户端套接字，如果请求的是网页则转到get_html发送
    # 网页给客户端，其他情况发数据,最后关闭客户端
    def handle(self, connfd):
        # 接收HTTP请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            connfd.close()
            return
        # 按行切割
        request_lines = request.splitlines()
        print(connfd.getpeername(), ':',
              request_lines[0])
        # 获取具体请求内容
        getRequest = str(request_lines[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd, getRequest)
        else:
            self.get_data(connfd, getRequest)
        connfd.close()

    # 发送网页给客户端
    # 解析客户端请求，并把响应发回给客户端
    def get_html(self, connfd, getRequest):
        if getRequest == '/':
            filename = self.static_dir + "/index.html"
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename)
        except Exception:
            # 没有找到网页
            responseHeaders = "HTTP/1.1 404 Not found\r\n"
            responseHeaders += '\r\n'
            responseBody = "<h1>Sorry,not found the page</h1>"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self, connfd, getRequest):
        urls = ['/time', '/tedu', '/hello']
        if getRequest in urls:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            if getRequest == '/time':
                import time
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody = "Tedu Python"
            elif getRequest == '/hello':
                responseBody = "Hello world"
        else:
            responseHeaders = 'HTTP/1.1 404 Not found\r\n'
            responseHeaders += '\r\n'
            responseBody = '<h1>Sorry,No data</h1>'
        # 将数据发送给客户端
        response = responseHeaders + responseBody
        connfd.send(response.encode())


if __name__ == "__main__":
    # 用户自己确定
    server_addr = ('0.0.0.0', 8000)
    static_dir = "./static"  # 存放网页

    # 创建服务器对象
    httpd = HTTPServer(server_addr, static_dir)
    # 启动http server
    httpd.serve_forever()
