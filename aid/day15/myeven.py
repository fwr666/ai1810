def myeven(start,stop):
    i = start
    while i < stop:
        if i % 2 == 0:
            yield i


        i += 1


evens = list(myeven(10,20))
print(evens)

for x in myeven(21,30):
    print(x)

    



