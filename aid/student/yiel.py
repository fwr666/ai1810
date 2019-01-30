import greenlet
import time 
import gevent

def test1():
    # time.sleep(2)
    print(12)
    g2.switch()
    print(13)
    g2.switch()

def test2():
    # time.sleep(2)
    print(23)
    g.switch()
    print(24)

g = greenlet.greenlet(test1)
g2 = greenlet.greenlet(test2)

g.switch()
