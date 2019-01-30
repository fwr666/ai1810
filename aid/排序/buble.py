s =[234,52,4,3]


for j in range(len(s)-1):
#次
    for x in range(len(s)-j-1):
        if s[x] > s[x+1]:
            s[x],s[x+1] = s[x+1],s[x]
        print(s)
    print('-----------')