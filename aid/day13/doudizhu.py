import random as rad
pokes = []#生成牌的列表
huase = ['\u2660','\u2663','\u2665','\u2666']
for x in range(1,14):
    if x == 1:
        poke = 'A'
        
    elif x == 11:
        poke = 'J'
    elif x == 12:
        poke = 'Q'
    elif x == 13:
        poke = 'K'
    else:
        poke = str(x)
    for i in range(4):
        s = huase[i] + poke
        pokes.append(s)

pokes.extend(['大王','小王'])
print(pokes)

p1 = rad.sample(pokes,17)
p1 = sorted(p1,key=lambda x:x[1:])
print('p1的牌是',p1)

a1 = []#发完p1剩下的牌，删除在总牌中删除p1
for x in pokes:
    if x not in p1:
        a1.append(x)

d = {
    'A':0,
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
}


p2 = rad.sample(a1,17)
print('p2的牌是',p2)
p2 = sorted(p2,key=lambda x:x[1:])
for x in p2:                         #打印出排序
    print(x[1:],end=' ')
print()
print('p2的牌是',p2)


a2 = []#发完p2剩下的牌
for x in a1:
    if x not in p2:
        a2.append(x)


p3 = rad.sample(a2,17)
p3 = sorted(p3,key=lambda x:x[1:])
print('p3的牌是',p3)


a3 = []#发完p3剩下的牌
for x in a2:#遍历剩下的牌a2
    if x not in p3:#如果不在p2手里,就说明还没发这张牌
        a3.append(x)

print('底牌是',a3)



