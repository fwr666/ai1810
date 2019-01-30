# def binary_search(list,item):

#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         if guess < item:
#             low = mid + 1
#     return None
# my_list = [1,2,3,4,5,6,7,8,9,12,453,34325]

# i = binary_search(my_list,7)
# print(i)









# def binary_search(list,item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low + high)//2
#         if list[mid] == item:
#             return mid
#         if list[mid] > item:
# def binary_search(list,item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low + high)//2
#         if list[mid] == item:
#             return mid
#         if list[mid] > item:
#             high = mid -1
#             continue
#         if list[mid] < item:
#             low = mid + 1
#             continue
#     return None
# my_list = [1,2,3,4,5,6,7,8,9,12,453,34325]

# i = binary_search(my_list,7)
#             high = mid -1
#             continue
#         if list[mid] < item:
#             low = mid + 1
#             continue
#     return None
# my_list = [1,2,3,4,5,6,7,8,9,12,453,34325]

# i = binary_search(my_list,7)
# print(i)



def binary_search(lis,iterm):
    low = 0
    high = len(lis)-1
    while low <= high:
        mid = (low + high)//2
        if lis[mid] == iterm:
            return mid
        if lis[mid] > iterm:
            hight = mid -1
        if lis[mid] < iterm:
            low = mid +1
    else:
        return None


my_list = [1,2,3,4,5,6,7,8,9,10]

a=binary_search(my_list,5)
print(a)                          


