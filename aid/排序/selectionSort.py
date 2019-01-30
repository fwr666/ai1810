#用来查找列表中最小的数
# def findSmallest(list):
#     smallest = list[0]
#     smallest_index = 0
#     for x in range(len(list)-1):
#         if list[x]<smallest:
#             smallest = list[x]
#             smallest_index = x
#     return smallest_index


#查找列表中最小的值

# def find_Smallest(list):
#     smallest = list[0]
#     smallest_index = 0
#     start = 0
#     while start < len(list):
#         if list[start] < smallest:
#             smallest = list[start]
#             smallest_index = start
#         start += 1
#     return smallest_index

# def selectionSort(arr):
#     newArr = [] 
#     for i in range(len(arr)):
#         smallest = find_Smallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr

# s = [12,1,3,2,15,1]

# print(selectionSort(s))

# def smallest(list):
#     smallest = list[0]
#     smallest_index = 0
#     for i in range(len(list)):
#         if list[i]<smallest:
#             smallest = list[i]
#             smallest_index = i
#     return smallest_index
# def selection(list):   
#     newarr = []
#     for x in range(len(list)):
#         smalles = smallest(list)
#         newarr.append(list.pop(smalles))
#     return newarr
# s = [12,1,3,2,15,1]
# print(selection(s))


                       



























