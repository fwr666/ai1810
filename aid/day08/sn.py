
#用于计算多项式的和
def fun(n):
    s = 0
    i = 1
    while i <= n: 
        s += 1/i
        i += 1
    return s


print(fun(21000))