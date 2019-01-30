




# 3. 分解质因数,输入一个正整数,分解质因数
#      如
#        输入: 90
#      打印
#        90 = 2*3*3*5
#     注: 质因数是指最小能被原数整数的素数(不包括1)






import math

def isprime(n):
    for x in range(2,int(math.sqrt(n)+1),2):
        if n % x == 0:
            return False
    return True


numb = int(input('输入一个数'))
i=2
a = []
n = numb
   
while i < numb:
    if isprime(i):
        if n % i == 0:
            n = n / i  #分解了，再分解
            a.append(str(i))
        else:
            i += 1
        
    else:
        i += 1

    pass
if a:
    print(a)
    ch = '*'.join(a)
    print(numb,'=',ch)
else:
    print(numb)

    