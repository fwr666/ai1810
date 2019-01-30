# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
from multiprocessing import Process
import sys
import signal  # 信号处理模块

# 客户端处理函数
# 功能：接收客户端的数据，并发回数据给客户端，完成是关闭进程
# 参数：客户端套接字
# 返回值：无


def handler(c):
    print("Connect from", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()
    sys.exit(0)  # 客户端退出子进程也退出

# 创建套接子

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 忽略子进程退出释放资源请求,交由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 接收客户端请求
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务端异常:", e)
        continue

    # 创建线程
    # 创建子进程，
    p = Process(target=handler, args=(c,))
    p.daemon = True
    p.start()
