class Student():
    def __init__(self,name,age,score=0):
        self.name = name
        self.age = age
        self.score = score
        
    def set_score(self,score):
        self.score = score
                                                                                                              
    def show_info(self):
        print(self.name,'今年',self.age,'岁','成绩:',self.score)
L = []
L.append(Student('小张',20,100))
L.append(Student('小李',28,98))
L.append(Student('小王','19'))
L[2].set_score(80)
for s in L:
    s.show_info()