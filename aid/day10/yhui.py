

def yh(n):
    sn = []
    if n == 1:
        return [1]
    for x in range(n):
        if x == 0 or x == n-1:
            sn.append(1)
        else:
            print(n)
            sn.append(yh(n-1)[x-1]+yh(n-1)[x])
            # print(sn)

    return sn

print(yh(5))

