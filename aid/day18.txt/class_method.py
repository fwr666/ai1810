

#此示例用类方法来访问类属性和改变类属性

class A:
    v = 1

    @classmethod
    def get_v(cls):   #cls----->class
        return cls.v
    
    @classmethod
    def set_v(cls,v):
        cls.v = v

print(A.v)
print(A.get_v())
 
a1 = A()
a1.v = 999
a1.set_v(666666)


print(A.get_v())
print(A.v)