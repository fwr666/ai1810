class Human:
    '''此示例示意类属性'''
    count = 0
    def __init__(self,name):
        print(name,'对象被创建')
        self.name = name
        self.__class__.count +=1
    def __del__(self):
        print(self.name,'对象被销毁')
        self.__class__.count -= 1

L = [Human('孙悟空'),Human('猪八戒')]
h1 = Human('沙僧')
print('现在共有',Human.count,'对象')
del L
print('现在有',Human.count,'对象')