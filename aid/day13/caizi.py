import random as rad
x = rad.randint(0,100)




while True:
    print(x)
    y = int(input('请输入一个数字:'))


    if x == y:
        print('恭喜您猜对了')
        break
    if x > y:
        print('您猜小了')
    if x < y:
        print('您猜大了')