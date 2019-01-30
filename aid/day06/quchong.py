L = [1,2,234,52,1,4,2,6,2,42,2,31,432,234,5,3]
L2 = []
L3 = []
for x in L:
    if x not in L2:
        L2.append(x)
    if L.count(x) == 2 and (x not in L3):
        L3.append(x)
print(L2)
print(L3)

