
# def mysum(n):
#     s = 0
#     i = 1
#     while i <= n:
#         s += i
#         i += 1
#     return s

# print(mysum(100))

def fun(n):
    return sum(map(lambda x:x**x,range(1,n+1)))
print(fun(3))