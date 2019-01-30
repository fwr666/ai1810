# 练习：
# 　　写一个计算公式的解释执行器，已知有如下一些函数

def myadd(x,y):
    return x + y
def mysub(x,y):
    return x - y
def mymul(x,y):
    return x * y


def get_func(op):
    if op == '加' or op == '+':
        return myadd
    if op == '减' or op == '-':
        return musub 
    if op == '乘' or op == '*':
        return mymul

def main():
    while True:
        s = input('请输入计算公式:')
        L = s.split(' ')
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print('结果是',fn(a,b))
main()