
# def story():
#     print('从前－－')
#     story()
# story()

#间接调用
# def fa():
#     print('666')
#     fb()
# def fb():
#     print('555')
#     fa()
# fa()

#recursion
# def fx(n):#n在某一个空间内
#     print("递归进入第",n',层)
#      if n == 3: 
#         fx(n+1)
#         print('递归退出第：'n=)
#     fx(1 ) #创造一个数据对象
    
#     调用堆栈　　　　　　　
#     指针

#     每调用一次就产生一回

# def myfac(n):
        
#     if n == 1:
#         return 1

#     else:
#         if n == 0:
#             return 1
#         s = n * myfac(n-1)
#         return s
# print(myfac(5))
# # 递归的含义：　　
# 　　　　　见递归

def mysum(n):
    if n == 1:
        return 1
    else:
        s = n + mysum(n-1)#先假设我的函数已经实现了原有的功能,逐渐从未知到已知，
        return s
print(mysum(100))

def get_age(n):
    if n == 1:
        return 10
    else:
        s = 2 + get_age(n-1)
        return s
print(get_age(3))
print(get_age(5))
