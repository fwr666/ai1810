def insertion_sort(lst):
    for x in range(1,len(lst)):
        i = lst[x]
        for y in range(x,0,-1):
            if lst[y-1] > i:
                lst[y] = lst[y-1]
            else:
                break
        lst[y-1] = i
    return lst

a = [55,22,1,2,3,53,2,43]

print(insertion_sort(a))

for x in range(1,4,1):
    if x == 2:
        break
print(x)