# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socketserver import *

# 创建服务器类
# class Server(ForkingMixIn,TCPServer):
# class Server(ThreadingMixIn,TCPServer):

# 多进程和TCP服务器


class Server(ThreadingTCPServer):
    pass

# 具体请求处理类
# 功能：处理客户端发来的数据
# 参数：流式套接字请求 StreamRequestHandler
# 返回值：无


class Handler(StreamRequestHandler):
    # 具体处理方法

    def handle(self):
        print("Connect from", self.client_address)
        while True:
            # self.request就是accept返回的套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')

# 创建服务器对象,绑定处理类
server_addr = ('0.0.0.0', 8888)
server = Server(server_addr, Handler)  # 第一个是请求地址，第一个参数是处理函数
server.serve_forever()  # 启动服务
