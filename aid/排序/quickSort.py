# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10,5,2,3]))

# def quicksort(array):
    
#     if len(array)<2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i<=pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# s = [6,3,12,5,23,4,2,3,1,111,1]

# print(quicksort(s))


# def quicksort(arr):
#     if len(arr)<2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

        

# s = [6,3,12,5,23,4,2,3,1,111,1]

# print(quicksort(s))

def quicksort(lst):
    if len(lst) < 2:#列表可能为空
        return lst
    else:
        pivot = lst[0]
        lesser = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
import random
s = []
for x in range(4):
    r = random.randint(1,1000)
    s.append(r)
print(quicksort(s))
# # s.sort()
# print(s)

# def quicksort(lst):
#     if len(lst)<2:

