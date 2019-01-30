class Human():
    '''此类示意类属性'''
    count = 0#创建类属性（类变量）

print(Human.count)
Human.count = 19
print(Human.count)
h1 = Human()
h1.count = 100
print(h1.count)#优先访问实例属性，不存在时访问类属性
print(Human.count)

#类属性可以通过此类的对象的__class__属性直接访问
h1.__class__.count = 98
print(Human.count)
