begin = int(input("请输入开始的数字:"))
end = int(input("请输入结束的数字:"))

L = [x for x in range(begin,end) if x%2==0]
print(L)