# 2. 输入一个字符串,把输入的字符串中的空格全部去掉,打印
#     出处理后的字符串的长度及内容
s = input("请输入字符串")
s = s.replace(' ','')
print("处理后的长度为",len(s),'内容为',s)