import time
n = 10000000000

count = 0
t1=time.time()
i = 1
while i < n:
    count +=1
    i /= 0.999999
t2=time.time()

t = t2 - t1
print(count)
print('每秒计算次数是',23025840/t)
