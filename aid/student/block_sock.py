from socket import *
from time import sleep,ctime

#创建套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)
# sockfd.setblocking(False)

#超时检测
sockfd.settimeout(4)
n = 0

while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()#阻塞等待
    except timeout:
        print('滚出克')
        break
    except BlockingIOError:
        sleep(2)
        n += 2
        print('等待连接%dsec'%n,ctime())
    else:
        print("Connect from",addr)
        data = connfd.recv(1024)
        print("Receive:",data.decode())
        n = 0

import select
select