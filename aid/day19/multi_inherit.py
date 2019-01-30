#多继承名字冲突问题实例

class A:
    def m(slef):
        print('A.m()被调用')
    
class B:
    def m(self):
        print('B.m()被调用')

class AB(B,A):
    pass

ab = AB()
ab.m()