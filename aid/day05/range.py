# 练习：
# 　１．用for语句打印１～２０的整数，打印在一行内
# 　　２．求１００以内有哪些整数与自身+1的乘积再对
# 　　　　１１求余等于８（包含１００）
print('-----------------------')
for x in range(1,21):
    print(x,end = ' ')
print()


print('-----------------------')
for x in range(101):
    if x*(x+1)%11 == 8:
        print(x,end = ' ')
print()

s = 0
for x in range(1,100,2):
    s += x 

print(s)
