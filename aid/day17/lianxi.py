# class Human:
#     def set_info(self,name,age,address='不详'):
#         self.name = name
#         self.age=age
#         self.address=address
#     def show_info(self):
#         print(self.name,'今年',self.age,'岁','家庭住址',self.address)
# h1 = Human()
# h1.set_info('小张',20,'北京朝阳区')
# h2 = Human()
# h2.set_info('小李',18)
# h1.show_info()
# h2.show_info()

class Car:
    '''此类定义一个小汽车类'''
    def __init__(self,c,b,m):
        self.color = c
        self.brand = b
        self.model = m
        print('初始化方法被调用')

    def run(self,speed):
        print(self.color,self.brand,self.model,'小汽车正在以',speed,'公里/小时的速度行驶')

a4 = Car('红色','法拉利','s')
a4.run(199)