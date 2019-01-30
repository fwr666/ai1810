

# xrange([start],stop,[step])


def myxrange(start,stop=None,step=1):
    if stop == None:
        stop = start
        start = 0
    try:
        if step > 0:
            while start < stop:  
                yield start
                start += step
        elif step < 0:
            while start > stop:
                yield start
                start += step
    except StopIteration:
        return 



for x in myxrange(10,5,-2):
    print('--------',x)

s=(x ** 2 for x in myxrange(1,10,2))




# j = iter(s)
# print('j',j)

# he = 0
# while True:
#     try:
#         i=next(j)
#         he += i
#         print(i)
       
#     except StopIteration:
    
#         break 
# print(he)

    
