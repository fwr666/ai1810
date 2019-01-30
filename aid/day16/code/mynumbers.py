#此程序用于保存用户输入的整数
n = open('mynumbers.txt','w')
try:
    while True:
        num = int(input('请输整数，-1结束'))
        if num < 0:
            break
        else:

            n.write(str(num))
finally:
    n.close()

mf = open('mynumbers.txt','rt')
x = mf.read()
mf.close()
print(x)
