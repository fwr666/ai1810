# try:
#     fw = open("mynumbers.txt",'w')
#     try:
#         while True:
#             n = int(input("请输入正整数"))
#             if n < 0:
#                 break
#             fw.write(str(n))
#             fw.write('\n')
#     finally:
#         fw.close()
# except OSError:
#     print('打开失败')
# except ValueError:
#     print('输入内容错误')
fr = open("mynumbers.txt",'r')
for x in fr:
    print(x)