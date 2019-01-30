# ，写一个程序，输入三行文字，将这三行文字保存与一个列表中L中，
# 　　　并打印这个列表
# s = list(input(""))

# L = []

# L =L+s  #可迭代对象
#  print(L)

# a = input('请输入')
# b = input('请输入')
# c = input('请输入')
# L = [a,b,c]
# print(L)


# L2 = []
# L2 += [a]
# L2 += [b]
# L2 += [c]
# print(L2)
# 练习，写一个整数，让用户输入很多个正整数，当输入负数时结束输入
# 　　将用户输入的数字存于列表中
# 　１）然后打印这个列表
# 　２）计算出这些数字的和，然后打印出这些和

L = []
s = 0
whileTrue:
    n = int(input('请输入正整数：'))
    if n < 0:
        break
    else:
        L += [n]
        s +=n
print(L)
print('和是：',s)
]p'