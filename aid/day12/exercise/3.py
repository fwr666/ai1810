# #  3. 编写函数fun 基功能是计算下列多项式的和
#     Sn = 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!
#     (建议用数学模块中的factorial)
#       求当n得20时 Sn的值
#     即:
#       print(fun(20))  # 2.718281828...
import math
# def fun(n):
#     sn = 0
#     for x in range(0,n+1):
#         sn += 1/math.factorial(x)
#     return sn
# def fun(n):
#     if n == 0:
#         return 1
#     else:
#         return 1/math.factorial(n)+fun(n-1)


def fun(n):
    sn = 0
    for fenmu in map(math.factorial,range(n + 1)):
        sn += 1 / fenmu
    return sn
print(fun(20))

    
    