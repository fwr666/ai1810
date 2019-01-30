#猴子问题

# nums = []
# n = 1
# b =1
# a = 1
# # n = (n + 1)*2

# while n <=10:
#     b=(a+1)*2
#     nums.append(b)
#     a = b
#     n += 1
# print(nums)
def f(n):
    if n == 10:
        return 1
    else:
        return f(n+1)*2+2
print(f(1))