# #while1.py
# #此示例用循环语句打印20行'hello'
# i = 1
# while i <= 20:
#     print("hello")
#     i += 1#改变i的绑定,让其增大，逐渐靠近20

# #while2.py
# n = int(input("请输入一个整数"))
# i = 1#此变量用来控制循环变量次数为 n 次
# while i <= n:
#     print('这是第%d行'%i)
#     i += 1#i增大


# n = int(input("请输入一个整数"))
# i = 1
# while n >= i:
    
#     if n<20 and  n % 5 == 0:
#         print() 
#     print('%d'%n,end = ' ') 
#     n -= 1
# else:
#     print()


# n = int(input("高度"))
# i = 1
# while i <= n:
#     if i == 1 or i == n:
#         print('*'*n)
#     else:
#         print('*'+' '*(n-2)+'*')
#     i += 1

#1~100============================
# n = int(input("数字"))
# i = 1
# s = 0
# while i <= n:
#     s += i
#     i += 1
# print(s)

# 练习：
# 　　输入一个数，打印指定宽度的正方形
# 　　如：请输入正方形宽度：５
# 　打印如下：
# 　　　１２３４５
# 　　　１２３４５
# 　　　１２３４５
# 　　　１２３４５
# 　　　１２３４５

# n = int(input("请输入正方形宽度:"))
# j = 1
# while j <= n:
#     i = 1
#     while i <= n:
#         print(i,end = ' ')
#         i += 1
#     print()
#     j += 1


# j = 1
# while j <= 9:
#     i = 1
#     while i <= j:
#         print('%d*%d=%d'%(j,i,i*j),end = ' ')
#         i += 1
#     print()
#     j += 1

# i = 1
# while i <= 6:
#     print("循环开始时:i=",i)
#     # if i == 3:
#     #     break
#     print('循环结束时:i=',i)
#     i += 1
# else:
#     print('子句')
# print('程序结束')

# 练习：
# 　　让用户任意输入一些整数，当输入负数时结束输入：
# 　当输入完成后，打印用户输入的所有整数的和  
su = 0
while True:
    n = int(input("请输入数字"))
    if n < 0:
        break
    su +=  n

print('您输入的这些数的和是：',su)


















