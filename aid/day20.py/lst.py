class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return ('Mylist(%r)'%self.data)

    def __add__(self,rhs):
        v = self.data + rhs.data
        return Mylist(v)
    
    def __mul__(self,rhs):
        # v = self.data * rhs
        return Mylist(self.data * rhs)

    def __rmul__(self,lhs):
        print('__rmul__被调用')
        return (Mylist(self.data * lhs))

    def __iadd__(self,rhs):
        self.data.extend(rhs.data)#self.data +=rhs.data
        return self

    def __neg__(self):
        gen = (-x for x in self.data)
        return MyList(gen)

    def __contains__(self,key):
        return key in self.data      


    def __getitem__(self,i):
        return self.data[i]

    def __setitem__(self,i,v):
        print("__setiem__方法被调用",i,v)
        self.data[i] = v


L1 = Mylist([1,-2,3,])
print(31 in L1)
print(L1) 
L2 = Mylist([4,5,6])
L3 = L1 + L2
print(L3)
L4 = L1 * 2
print(L4)
L6 = 2 * L1
print(L6)
print('2',L6[2])

L1[1] = +2
print(L1)