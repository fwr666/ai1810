

# #插入排序
# import random

# lst = []
# for _ in range(5):
#     a = random.randint(1,30)
#     lst.append(a)
# # print(lst)
# # lst.sort()
# print(lst)
# j=1
# while j < len(lst):
#     i = j
#     a = lst[i]
#     while i > 0:
#         if a >= lst[i-1]:
#             break  
#         if a < lst[i-1]:
#             lst[i] = lst[i-1]

#         i -= 1
#     lst[i] = a
#     j += 1
# print(lst)

#二分查找
# def binary_search(L,iterm,low,high):
#     mid = (low + high) // 2
#     if L[mid] == iterm:
#         return mid
#     elif L[mid] > iterm:
#         high = mid -1
#         return binary_search(L,iterm,low,high)
#     elif L[mid] < iterm:
#         low = mid +1
#         return binary_search(L,iterm,low,high)





# print(lst)

# import random
# ls = []
# for _ in range(10):
    
#     a = random.randint(1,50)
#     ls.append(a)
# print(ls)
ls = [45, 18, 8, 22, 27, 32, 31, 37, 7, 26]
for x in range(1, len(ls)):
    f = ls[x]
    for y in range(x-1, -1, -1):
        if f < ls[y]:
            ls[y+1],ls[y] = ls[y], ls[y+1]
        else:
            break
    # print(ls[y-1])
    # print(y)
    # ls[y] = f
print(ls)


ls = [45, 18, 8, 22, 27, 32, 31, 37, 7, 26]
for x in range(1, len(ls)):
    pos = x
    f = ls[x]
    for y in range(x-1, -1, -1):
        if ls[y] > f:
            ls[y+1] = ls[y]
            pos = y
        else:
            # pos = y + 1
            break
    ls[pos] = f
print(ls)
    
        
    
