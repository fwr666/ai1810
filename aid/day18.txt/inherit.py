# inherit.py

class Human():
    '''定义一个人类的基类'''
    def say(self,what):
        print('说:',what)
    def walk(self,distance):
        print('走了:',distance,'公里')

class Student(Human):
    def study(self,subject):
        print('学习',subject)

class Teacher(Human):
    def teach(self,subject):
        print('教',subject)

h1 = Human()
h1.say('天气变冷了')
h1.walk(5)

s1 = Student()
s1.say('666')
s1.study('Eglish')
s1.walk(6)

t1 = Teacher()
t1.say('hello')
t1.walk(4)
t1.teach('777')
