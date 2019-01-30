# 4.输入一个开始的整数用变量begin绑定
#  输入一个结束的整数用变量end绑定
#  打印从begin 到 end （不含end）之间的每个整数打印在一行内

begin = int(input('请输入开始数字'))
end = int(input('请输入结束数字'))
i = 1
while begin < end:
    print(begin,end=' ')
    if i % 5 == 0:
        print()
    
    begin += 1
    i += 1
else:
    print()