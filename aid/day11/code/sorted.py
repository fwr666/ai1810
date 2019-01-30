# 练习：
# 　　将以下列表中的数据进行排序
import math
L = [(1,5),(3,9),(4,1),(5,8),(5,3)]

def a2(b):
    return b[1]
L2 = sorted(L,key=a2)
print('L2=',L2)
L3 = sorted(L,key=lambda x: x[1],reverse=True)
print('L3=',L3)

def distance(a):
    distance = (a[0]**2 + a[1]**2)
    return distance

L4 = sorted(L,key=distance)
print('L4=',L4)