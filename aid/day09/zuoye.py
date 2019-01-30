# 　１．写一个函数 isprime(x) 判断x 是否是素数，如果为素数则返回
#     　　　　True,否则返回False
#        2.写一个函数prime_m2n(m,n)返回从m开始，到n结束(不包含n))范围内
#        的素数，返回这些素数的列表，并打印
#        如：
#        　　L = prime_m2n(10,20)
#         print(L) #[11,13,17,19]

#        3.写一个函数primes(n),返回指定范围内n（不包含n）的全部素数的列表
#        　　并打印这列素数的列表
#        　　　　L
def isprime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        else:
            return True
# n = int(input('xxx'))

# print(isprime(n))


def prime_m2n(m,n):
    # a = []
    # for x in range(m,n):
    #     if isprime(x):
    #         a.append(x)
    # return a
    return [x  for x in range(m,n) if isprime(x)]
s = prime_m2n(0,20)
print(s)

def primes(n):
    return prime_m2n(2,n)
print(primes(100))