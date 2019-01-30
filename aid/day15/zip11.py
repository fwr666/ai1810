

#此示例示意实现一个含有两个形参的zip函数的实现方式
def myzip(iterable1,iterable2):
    it1 = iter(iterable1)   #得到iterable的迭代器
    it2 = iter(iterable2)
    try:
        while True:
            x1 = next(it1)
            x2 = next(it2)
            yield (x1,x2)
    except StopIteration:
        return

numbers = [10086,1,2,3]
names = ['a','b','c']

for t in myzip(numbers,names):
    print(t)
