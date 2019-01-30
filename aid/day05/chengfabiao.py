# １．写程序打印九九乘法表

for x in range(1,10):
    for y in range(1,x+1):
        print('%d*%d=%d'%(y,x,x*y),end = ' ')
    print()