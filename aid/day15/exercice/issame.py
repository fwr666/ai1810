
#   2. 写一个程序,从键盘输入一段字符串,用变量s绑定
#      1) 将此字符串转为字节串用变量b绑定,并打印出此字节串b
#      2) 打印字符串s的长度和字节串b的长度
#      3) 将字节串b再转换为字符串用变量s2 绑定,然后判断
#        s2 和 s是否相同

s = input('请输入一段字符串')

b = bytes(s,encoding='utf-8')
print(len(s))
print(len(b))
s2 = b.decode(encoding='utf-8')
print(s2)
print(s2 == s)
