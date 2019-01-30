# a,b = 0,1
# i = 1
# L = []
# while i <= 40:
#     L.append(b)
#     a,b = b,a+b
#     i += 1
# print('斐波那契数列',L)
# print(len(L))
L = [x for x in range(1,41)]
i = 0
while i<40:
    if i<=1:
        L[i]=1
    else:
        L[i]=L[i-1]+L[i-2]
    i +=1
print(L)