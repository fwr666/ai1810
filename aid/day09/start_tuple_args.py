# # start_tuple_args.py


# # 此示例示意星号元组形参的定义及使用
# def func(*args):
#     print('实参个数是',len(args))
#     print('args',args)

# func()
# print('-------------')
# func(1,2,3,4)
# print('-------------')
# func(1,2,3,4,'AAA','bbb')
# func(*'abcdefg')

# #元组还能表示先后顺序关系


# 练习：
# 　　写一个函数，mysum,可以传入任意个数字实参，返回所有实参的和

# def mysum(*args):
#     s = 0

#     for x in args:
#         s +=x 
#     return s

#方法二：
def mysum(*args):
    return sum(args)#传给ｓｕｍ一个可迭代对象

print(mysum(1,2))
print(mysum(1,2,3,4))
print(mysum(1,2,3,4,5,6,7,8))
print(mysum(-1))