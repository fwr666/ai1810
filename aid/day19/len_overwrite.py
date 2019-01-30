class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'Mylist%s'%self.data
    
    def __len__(self):
        '''此方法必须返回整数'''
        print('sss1')
        return len(self.data)
    def __abs__(self):
        print('sss')
        # L = [abs(x) for x in self.data]
        # lst = Mylist(L)
        return lst

    # def __bool__(self):
    #     for x in self.data:
    #         if bool(x)==False:
    #             return False
    #     return True

myl = Mylist([1,2,3,4,5])
# myl2 = abs(myl)
# print(myl)
# print(myl2)
# print(len(myl))
print(bool(myl))
if myl:
    print('真值')
else:
    print('假值')