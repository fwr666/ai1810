# def func(**kwargs):
#     print('关键字参数的个数是：',len(kwargs))
#     print('kwargs= ',kwargs)
# func(name = '喵喵',age = 3,address = 'mx')
# func(a = 1)
# func(v=1)#出错

def mymax(*args):
    if len(args) == 1:
        iterable = args[0]
        zd = iterable[0]
        for x in iterable:
            if x > zd:
                zd = x
    else:
        zd = args[0]
        for x in args:
            if x > zd:
                zd = x
    return zd
print(mymax((100,20,30)))
print(mymax(100,200))
print(mymax(1,2,3,9,1))

# def mymax(a,*args):
#     if len(args) == 0:
        
#         zd = a[0]
#         for x in a:
#             if x > zd:
#                 zd = x
#     else:
#         zd = a
#         for x in args:
#             if x > zd:
#                 zd = x
#     return zd
# print(mymax((100,20,30)))
# print(mymax(100,200))
# print(mymax(1,2,3,9,1))
# print(mymax(1))



# a = 100
# b = 200
# def fx(c):#fx也是全局变量，它绑定一个函数
#     d = 400
#     a = 333
#     print(a,b,c,d)
# fx(300)
# print(a,b)
# print(c,d)#c,d变量在此作用域内不存在











