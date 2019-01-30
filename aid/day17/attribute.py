class Dog:
    def eat(self,food):
        print(self.color,self.kinds,'小狗正在吃',food)
        self.last_food = food
    def food_info(self):
        print(self.color,self.kinds,self.last_food)

dog1=Dog()
dog1.color = '白色'
dog1.kinds = '京巴'
print(dog1.color,dog1.kinds)
dog1.eat('骨头')
dog2 = Dog()
dog2.color='灰色'
dog2.kinds='哈士奇'
dog2.eat('狗粮')
dog2.food_info()