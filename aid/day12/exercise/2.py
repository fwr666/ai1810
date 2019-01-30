import time
h = int(input('请输入小时'))
m = int(input('请输入分钟'))
while True:
    time.sleep(1)
    dd = time.localtime()
    if dd[3] == h and dd[4] == m:
        print('时间到')
        break