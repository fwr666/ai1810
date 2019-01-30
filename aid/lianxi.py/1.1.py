# i = 1
# while i <= 4:
#     print(('*'*(2*i-1)).center(7),end = '')
#     print()
#     i += 1

# def s(n):
#     if n == 1:
#         return 1
#     else:
#         print('haha',n)
#         return s(n-1)+n
# print(s(100))
a = [x for x in range(1,101)]
def b(a,i,low=0,high=len(a)-1,count=0):
    mid = (low+high)//2
    if a[mid] == i:
        count += 1
        return mid,count
    elif a[mid] < i:
        count += 1
        low = mid
        return b(a,i,low,high,count)
    elif a[mid] > i:
        count += 1
        high = mid
        return b(a,i,low,high,count)
# a = [x for x in range(1,101)]

print(b(a,47))    