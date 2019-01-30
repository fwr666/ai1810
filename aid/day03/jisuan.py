
def myadd(x, y):
    return x + y

def mysub(x, y):
    return x - y

def mymul(x, y):
    return x * y

def get_func(op):
    if op == '+' or op == '加':
        return myadd
    elif op in ('-', '减'):
        return mysub
    elif op in ('*', '乘'):
        return mymul

def main():
    while True:
        s = input("请输入计算公式: ")  # 10 加 20
        L = s.split()  # L = ['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30

main()