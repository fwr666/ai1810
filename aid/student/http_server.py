from socket import *


#执行函数处理客户端请求
def handle(connfd):
    print('Connect from',connfd.getpeername())
    request = connfd.recv(4096)
    request_lines = request.splitlines()
    for line in request_lines:
        print(line)

    #给浏览器客户端返回响应
    try:
        f = open("index.html")
    except IOError:
        response = "HTTP/1.1 404 Not found\r\n"
        response +='\r\n'
        response += '===sorry not found the page=='
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        response += f.read()
    finally:
        #将结果发送给客户端
        connfd.send(response.encode())
        f.close()


#在主函数创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("Listen to the port 8000...")
    while True:
        connfd,addr = sockfd.accept()#等待接收客户端的连接
        #处理客户端请求
        handle(connfd)
        connfd.close()
main()