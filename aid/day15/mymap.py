

def myfilter(func,iterable):
    it = iter(iterable)
    while True:
        try:
            x = next(it)
        except StopIteration:
            return
        if func(x):
            yield x
s = myfilter(lambda x:x%2==0,range(10))
for x in s:
    print(x)