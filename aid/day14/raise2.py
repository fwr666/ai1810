#此示例示意用　raise 语句来传递错误信息

def f1():
    n = int(input("请输整数:"))

def f2():
    try:
        f1()
    except ValueError as err:
        print('f1函数内出错')
        print('f2',err)
        raise

try:
    f2()
except ValueError:
    print('f2内发生了ValueError类型的错误')