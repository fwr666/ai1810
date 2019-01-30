#本函数实现找任意数的质因子,并用质因子表达式表达本数
# 实现思路
    # 遍历２到ｎ的数字　看是否被整除
    # 整除后得到的数字　再去整除
# 程序实现　
    # 用生成函数　思想　模仿ｍａｐ函数
def isprime(n):
    if n<2:
        return False
    else:
        for x in range(2,n):
            if x%2==0:
                return False
        
        return True  

def myfilter(fx,iterble):
    for x in iterble:
        if fx(x):
            yield x
def zhiyinzi(n):
    for x in myfilter(isprime,range(n+1)):
        while True:
            if n%x==0:
                yield x
            else:
                break
def print_zhiyinzi(n):
    for x in zhiyinzi(n):
        print(x,end='*')
# import time
# nn = int(input('请输入nn'))
# t1 = time.time()
print_zhiyinzi(100)
# t2 = time.time()
# t = t2 -t1
# print('时间',t)
# #241242532

            
