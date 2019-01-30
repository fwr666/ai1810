# 练习：
# 　１．输入任意一段字符串,写程序做如下两件事：
# 　　　１）。计算出空格的个数，并打印个数
# 　　　２）。计算出字符串中全部英文字符的个数
# 　　　　（注：英文字符的编码值为0~127,可用ord(x)函数进行判断）
#   2.能否用while实现以上

# s = input('请输入一段字符串:')
# count = 0
# english_count = 0
# for ch in s:
#     if ch == ' ':
#         count += 1
#     if 0 <= ord(ch) <=127:
#         english_count +=1
# print(ch)
# print(count)
# print('英文字符的个数为:',english_count)


# i = 0
# blank_count = 0
# english_count = 0
# while index < len(s):
#     if s[index] == ' ':
#         blank_count += 1
#     if 0 <= ord(s[index]) <=127:
#         english_count += 1
#     index += 1 
# print(blank_count)
# print('英文字符的个数为:',english_count)

# i = 6
# for x in range(1,i):#只生成一次,后面修改i也没有用
#     print('x=',x,i)
#     i -= 1#
# for x in 'ABC':
#     for y in "123":
#         print(x+y)
# n = int(input('请输入数字'))
# n += 1
# for x in range(1,n):
#     for y in range(1,n):
#         print(y,end = +' ')
#     print()
# print('-------------------------------')

# for y in range(1,n):
#     for x in range(y,n+y-1):#写个循环
#         print(x,end = '  ')
#     print()
# '''
# 666
# '''

# w = int(input('-'))
# for x in range(1,w+1):
#     for y in range(x,x+w):
#         print(y,end=' ')
#     print()#换行
# print('---')