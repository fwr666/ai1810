# for num in range(10):
#     if (num % 2 == 1):
#         continue
# print(num)

# print('   *','\n','  ***','\n', '*****')
# class A:
#     v = 100
#     def __init__(self):
#         self.v = 200
# a1 = A()
# a2 = A()
# del a2.v
# print(A.v)
# print(a2.v)
# print(a1.v)
# print(a1.__class__.v)

# class Human: 
#     def __init__(self, name="Anonymous", age=0, *args): 
#         self.name,self.age = name, age 
#     def infos(self): 
#         print(self.name, self.age) 
# class Teacher(Human): 
#     def __init__(self, name, age, address=""): 
#         self.address = address 
#     def infos(self):
#         print(self.name, self.age, self.address)
# # t1 = Teacher("Mr. zhang", 35)
# # t1.infos()
# h1 = Human("Mr. zhang", 35, "北京市朝阳区", "其它信息不详")
# h1.infos()
# # t1 = Teacher("Mr. zhang", 35)
# # t1.infos()
# # t1 = Teacher("Mr. zhang", 35)
# # t1.infos()
# h1 = Human()
# h1.infos()


L1 = [1, 2, 3]
L2 = [L1, 4, 5]
L3 = L2
L4 = L3.copy()
L1[1] = 10
L3[1] = 40
L4[2] = 50
print(L2)
print(L3)
print(L4)