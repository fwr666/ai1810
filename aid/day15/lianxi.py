L = [2,3,5,7]
def a(L):
    for a in L:
        yield a**2 +1

for x in a(L):
    print('--',x)


a = (x ** 2 + 1 for x in L)
print(a)
for x in a:
    print (x)

b = [x ** 2 + 1 for x in L]
print(b)