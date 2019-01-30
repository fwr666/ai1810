def myfilter(func,iterable):
    for x in iterable:
        if func(x):
            yield x

for i in myfilter(lambda x:x%2==1,range(10)):
    print(i)

def myfilter(func,iterable):
    it = iter(iterable)
    while True:
        try:
        x = next(it)
        if func(x):
            yield x
        except StopIteration:
            return