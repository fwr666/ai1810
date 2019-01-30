# #经理
# s1 = {'曹操','刘备','孙权'}

# #技术员
# s2 = {'曹操','孙权','张飞','关羽'}

# print('即是经理也是技术员的有：',s1&s2)
# print('是技术员，但不是经理的有:',s2-s1)
# print('是经理，但不是技术员的有:',s1-s2)
# print('张飞是经理吗','张飞' in s1)
# print('身兼一职的有：',s1^s2)
# print('经理和技术员共有：',s1|s2)

# 写一个函数myadd，此函数中的参数列表有两个参数x,y
# 此函数的功能是打印调用参数的和,即x + y

# def myadd(x,y):
#     print(x+y)

# myadd('abc')
# event = []
# def even(x):
#     for x in range(x,2):
#         print(x)
# even(199)
# even(10)

# function　功能

# 1.写一个函数　mymax, 实现返回两个数的最大值：

# def mymax(x,y):
#     if x > y:
#         return x
#     else:
#         return y

# print(mymax(12,2))

# def myadd(x,y):
#     return x + y
# a = int(input('请输入第一个数：'))
# b = int(input('请输入第二个数：'))
# print(a,'+',b,'的和是',myadd(a,b))

def input_number():
    L = []
    while True:
        num = int(input('请输入整数:'))
        if num < 0:
            break
        elif:
            L.append(num)
    return L

L = input_number()
print('用户输入的最大值是：',max(L))
print('用户输入的最小值是：',min(L))
print('用户输入往返全部数的和是：',sum(L))

