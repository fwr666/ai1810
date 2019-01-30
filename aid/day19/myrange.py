class Myrange:
    def __init__(self,start,stop=None,step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        print('111')
        return MyRangeIterator(self.start,
                                self.stop,
                                self.step)

class MyRangeIterator:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            r = self.start
            self.start += self.step
            return r

L = list(range(10))
print(L)













#         if self.stop == None:
#             self.stop = self.start
#             self.start = 0
#         if self.step > 0:
#             if self.start>self.stop:
#                 raise StopIteration
#             return self.start
#             self.start += self.step
#         elif self.step < 0:
#             if self.start < self.stop:
#                 raise StopIteration
#             return self.start
#             self.start += self.stop
            
# L = list(Myrange(5))
# print(L)           

# class MyListIterator:
#     def __init__(self,lst):
#         self.data2 = lst
#         self.index = 0

#     def __next__(self):
#         if self.index >= len(self.data2):
#             raise StopIteration
#         r = self.data2[self.index]
#         self.index += 1
#         return r