import time
def fenjie(numb):
    a = []
    i = 2
    n = numb

  
    while i < numb:
        if n % i == 0:
            a.append(i)
            n /= i
            if n == 1:
                break
            continue
        # i += 1
        if i < 3:
            i += 1
        else:
            i += 2
    print(numb,'可分解为',a)

# for x in range(10000,200000):
fenjie(241354723)


# 123124134
#30s
# 12312413
# 3s
# 1231241