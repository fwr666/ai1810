from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#添加关注列表
rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    for r in rs:
        if r is s:
        c,addr = r.accept()
        print("Connect from",addr)
        rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            with open('xxx.txt','rb') as f:
                f.write(data)
            print("Receive from %s:%s"%(r.getpeername,
              data.decode()))
            r.send(b'Receive')
    for w in ws:
        pass
    for x in xs:
        pass
s.close()

