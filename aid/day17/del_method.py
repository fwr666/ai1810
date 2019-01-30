#此示例示意　析构方法的定义和使用

class Car:
    def __init__(self,info):
        self.info = info
        print(info,'对象被创建')
    def __del__(self):
        print(self.info,'对象被销毁')
c1 = Car('byd e6')
# del c1
c1 = None
input('回车继续')
print('程序正常退出')