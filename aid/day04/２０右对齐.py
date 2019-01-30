a = input('请输入第一行：')
b = input('请输入第二行：')
c = input('请输入第三行：')
x = max(len(a),len(b),len(c))
fmt = '%'+str(x)+'s'

print(fmt%a)
print(fmt%b)
print(fmt%c)