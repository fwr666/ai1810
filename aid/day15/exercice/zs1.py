
import math
import time
def sushu(n):
    a=[2,3]
    for x in range(4,n):
        for y in a[:int(math.sqrt(len(a)))+1]:
            if x % y == 0:
                break
        else:
            a.append(x)
    t1=time.time()
    print(a)
    t2=time.time()
    t=t2-t1
    print('时间',t)
sushu(2000000)
