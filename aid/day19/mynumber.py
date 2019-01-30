


class M:
    def __init__(self,value):
        '''初始化方法'''
        self.data = value
    def __str__(self):
        return 'sss!!'+str(self.data)
    def __int__(self):
        return int(self.data)
    

n1 = M('100')
i = int(n1)#已经是int类
print(i)
print(str(n1))
print(n1)

