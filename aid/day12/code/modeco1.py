

#定义装饰器函数,并装饰myfunc
#装饰器的原理是替换被装饰函数的一个变量绑定关系
#用装饰器语法实现方法见 mydeco4.py
def mydeco(fn):
    def fx():
        print('++++++')
        fn()
        print('------')
    return fx



def myfunc():
    print('函数被调用了')

myfunc = mydeco(myfunc)#装饰器的开关

myfunc()
myfunc()
myfunc()











