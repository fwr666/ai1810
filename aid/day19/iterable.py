class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)'%self.data

    def __iter__(self):
        '''有此方法的对象可以用iter(obj)来获取迭代器'''
        return MyListIterator(self.data)#'迭代器                                                                                                                                                                                                                               '

class MyListIterator:
    def __init__(self,lst):
        self.data2 = lst
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data2):
            raise StopIteration
        r = self.data2[self.index]
        self.index += 1
        return r


myl = Mylist([1,2,3,4,5])
for x in myl.data:
    print(x)