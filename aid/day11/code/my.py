# def myadd(x,y):#此函数没有访问全局或外部嵌套函数的变量
#     print(x + y)
# print(myadd(100,200))

# def power2(x):
#     return x ** 2
# for x in map(power2,range(1,10)):
#     print(x)

# for x in map(pow,[1,2,3,4],(4,3,2,1)):
#     print(x)

# 求　1**2 + 2**2 +3 

# print(map(pow, range(1,10),9*[2]))
# print(sum(map(pow, range(1,10),9*[3])))
# print(sum(map(pow, range(1,10),range(9,0,-1))))

# # def sn(n):
# #     s = 0
# #     for x in range(1,101):
# #         s += x
# #     return s
# # sn(10)   

# def pow2(x):
#     return x ** 2
# s = 0
# for x in map(pow2,range(1,10)):
#     s += x
# print('和是',s)

# 练习：
# 　　用filter 函数将1 ~100 之间所有　素数prinme 存放与列表中

def isprime(x):
    isprime = True
    if x < 2 :
            isprime = False
            return isprime

    for i in range(2,x):
        if x % i == 0:
            isprime = False
            return isprime
    return isprime

# L = list(filter(isprime,range(100)))
L = [x for x in filter(isprime,range(100))]
print(L)
