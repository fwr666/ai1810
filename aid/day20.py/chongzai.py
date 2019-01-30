class MyNumber:
    def __init__(self,value):
        self.data = value

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self,other):
        print('MyNumer.__add__方法被调用')
        v = self.data + other.data
        return MyNumber(v)#创建一个新的对象并返回

    def __sub__(self,rhs):
        v = self.data - other.data
        return MyNumber(v)
n1 = MyNumber(100)
n2 = MyNumber(200)
print(n1)
# n3=n1.__add__(n2)
n3 = n1 + n2#等同于# n3=n1.__add__(n2)
print(n3)
n4 = n2 - n1
print(n4)











