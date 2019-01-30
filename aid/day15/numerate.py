names = ['中国移动','中国电信','中国联通']
# for t in enumerate(names,2):
#     print(t)

def myenumerate(iterable,start=0):
    # it1 = iter(iterable)
    # # it2 = iter(range(start,len(iterable)+start))
    # while True:
    #     try:
    #         # x1 = next(it2)
    #         x2 = next(it1)
    #         yield (start,x2)
    #         start += 1
    #     except StopIteration:
    #         return

    for x in iterable:
        yield (start,x)
        start += 1
for t in myenumerate(names,2):
    print(t)