#  练习：
#     　　输入一个字符，从尾向头输入这个字符串的字符
#     　　　如：
#     　　　　请输入：hello
#          打印如下：olleh
#         可以用while 语句　或for 语句　实现

s = input('请输入一段字符:')

# index = 0
# while index < len(s):
#     ch = s[len(s)-index-1]
#     print(ch)
#     index += 1
index = len(s) - 1
while index >= 0:
    print(s[index])
    index -= 1