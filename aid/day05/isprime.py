# ２．写一个程序，任意输入一个整数，判断这个数是否为素数
#  　　prime素数（也叫质数），是只能被１和自身整数的正整数
#  　提示：
#  　　　用排除法：
#  　　　　　当判断x是否为素数时，只要让ｘ分别除以2,3,4...x-1
#      只要有一次被整除，则ｘ不是素数，否则ｘ是素数

for n in range(2,100):
    #用一个变量作为标志
    flag = True

    for x in range(2,n):
        if n % x == 0:
            flag = False
           
            
            break
    if flag:
        print(n,'是素数')
    else:
        print(n,"不是素数")