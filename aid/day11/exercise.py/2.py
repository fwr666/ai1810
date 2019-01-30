def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)
# s = 0

# for x in range(1,25):
#     print(func(x))
    
#     s += func(x)

s = sum(map(func,range(1,21)))
print(s)
