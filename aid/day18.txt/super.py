# class A:

#     def work(self):
#         print('A.work被调用')

# class B(A):
#     def work(self):
#         print('B.work被调用')


# b = B()

# super(B,b).work()#借助b调用A类的方法
class Human:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def show_info(self):
        print('姓名：',self.name)
        print('年龄：',self.age)

class Student(Human):
    def __init__(self,n,a,s=0):
        super().__init__(n,a)
        self.score = s #在此类中添加新的属性
    
    def show_info(self):
        super().show_info()
        print('成绩',self.score)


s = Student('小张',20)
s.show_info()