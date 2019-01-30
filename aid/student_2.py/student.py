#学生类
class Student():
    L = []
    __slots__ = ['name','age','score']
    def __init__(self,name,age,score=0):
        self.name = name
        self.age = age
        self.score = score


    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

    def get_info(self):
        return (self.name,self.age,self.score)

    @classmethod
    def add_st(cls,st):
        cls.L.append(st)

    @classmethod
    def delet_st(cls,st):
        if st in cls.L:
            cls.L.pop(st)
        else:
            print('没有这个学生')



    def write_to(self,f):
        f.write(self.name)
        f.write(',')
        f.write(str(self.age))
        f.write(',')
        f.write(str(self.score))
        f.write('\n')






