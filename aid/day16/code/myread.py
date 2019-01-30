i = 0
mr  = open('info.txt')
while i < 3:

    x = mr.readline()

    s = x.split(' ')
    print(s[0],'今年',s[1],'成绩是',s[2])
    i += 1
