# 　　１．写程序求下列算式的值：
# 　　　　1/1 -1/3 + 1/5 -1/7 + ...(-/+)1/(2*n-1)的和，
# 求:
#   1)当n等于10000时，此算式的和并打印
#    2)将n 等于10000时算式的和乘以4,并打印其结果(3.14)
s = 0.0
n = 1.0
while n <=10000:
    k = (-1)**(n-1)
    j = 1/(2*n-1)
    s += k*j
    n += 1
print('%.30f'%s)
print('%.20f'%(s*4))