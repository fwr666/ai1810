
numbers = [1,2,3,4]
names = ['a','b','c',]
n = [2,3,4,5]
d = dict(zip(numbers,names))
print(d)
for name,numb in zip(names,numbers):
    print(name,'的客服电话是',numb)
    
