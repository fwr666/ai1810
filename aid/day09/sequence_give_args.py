def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)
L = [1,2,3]
T = (100,200,300)


#说明：  序列传参时，序列拆解的位置将与形参一一对应
myfun1(*T)
