class Mylist(list):
    def insert_head(self,n):
        # self.insert(0,n)
        self[0:0]=n

a = Mylist(range(3,6))
a.insert_head(2)
print(a)