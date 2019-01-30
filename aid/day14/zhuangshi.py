def fx(fn):
    def f1():

        fn()
        n += 3
     
    return f1



@fx
def f2():
    n = 2
    return n


print(f2())

