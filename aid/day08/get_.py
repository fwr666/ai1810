
# #得到用户输入的中文的个数
# def get_chinese_char_count(s):
#     count = 0
#     for ch in s:
#         if int(0x4e00)<=ord(ch)<=int(0x9FA5):
#             count += 1
#     return count

# s = input('请输入要统计的字符')

# count = get_chinese_char_count(s)
# print(count)

# for x in range(65535):
#     print(chr(x),end


# 汉诺塔递归：
#2*(n-1)+1
def hn(n):
    if n == 1:
        print('hh')
        return 1
    else:
        print('调用了',n)
        return hn(n-1)*2+1
print(hn(64))