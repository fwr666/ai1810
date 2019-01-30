# class Human:
#     #此__slots__列表限定Human类型的对象只能用一个age属性
#     __slots__ = ['age']
#     def __init__(self,age):


# print(Human.__slots__)

L = [1,2,3]
print(id(L))
def fun(aa):
    aa = [4,5,6]
    print('aa',id(aa))

fun(L)
print(id(L))