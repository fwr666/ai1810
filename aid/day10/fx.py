def f1():
    print('f1函数被调用了')

def f2():
    print('f2函数被调用了')

def fx(fn):
    print(fn)#打印函数的地址
    fn()

fx(f1)