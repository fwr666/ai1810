d = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

numb = input('输入罗马数字')
s = 0
start = 0
for x in numb:
    if d[x] > start:
        s = s + d[x] -2*start
    else:
        s = s + d[x]

    start = d[x]
print(s)   
