class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.money = 0
        self.skill = []#技能

    def teach(self,other,subject):
        print(self.name,'教',other.name,subject)
        other.skill.append(subject)

    def work(self,money):
        print(self.name,'上班赚了',money)
        self.money += money

    def borrow_from(self,other,money):
        print(self.name,'向',other.name,'借了',money)
        self.money += money
        other.money -= money

    def show_info(self):
        print(self.age,self.name,self.money,self.skill)

h1 = Human('张三',35)
h2 = Human('李四',15)
h1.teach(h2,'python')
h2.teach(h1,'王者荣耀')
h1.work(1000)
h2.borrow_from(h1,200)
h1.show_info()
h2.show_info()

