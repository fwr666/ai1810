#           *
#   3.用程序while语句生成如下字符串，并打印结果
#     1)'ABCDE...Z'
# #     2)'AaBb..XxYyZz'
# i = 0
# j = 65
# k = 97
# s = ''
# while i < 52:
#     if i % 2 == 0:
#         while j <= 90:
#             s += chr(j)
#             j += 1
#             break
#     else:
#         while k <= 122:
#             s += chr(k)
#             k += 1
#             break

#     i += 1
# print(s)

s = ''
i = 65
while i <= 90:
    s += chr(i)
    s += chr(i + 32)
    i += 1
print(s)