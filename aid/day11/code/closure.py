# money = 1000#全局变量的，不安全
# def child_buy(obj,m):
#     global money
#     if money > m:
#         print('买',obj,'花了',m)
#         money -= m
#     child_buy()

#创建一系列函数

def make_power(y):
    def fn(x):
        return x ** y
    return fn
