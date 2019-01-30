# #if .py
# #此示例示意if语句的执行过程及语句
# num = int (input('输入一个数'))
# if num % 2 == 0:
#     print('是偶数')
# else:
#     print('是奇数')
# num = int(input('请输入一个数字'))

# if num < 0:
#     print('num<0')
# if 50<=num<=150:
#     print('50<=num<=150')
# if num > 100:
#         print('num>100')

#输入一个季度1~4,输出这个季度有哪几个月，
#如果用户输入的不是1~4的整数，则提醒用户"您输错了

num = int(input('请输入月份'))
if num == 1:
    print('1,2,3')
elif num == 2:
    print('4,5,6')
elif num == 3:
    print('7,8,9')
elif num == 4:
    print('10,11,12')
else:
    print('您输错了')

n = int(input('请输入月份'))

if n==1 or n==2 or n==3:
    print('第一季度')
elif n==4 or n==5 or n==6:
    print('第二季度')
elif n==7 or n==8 or n==9:
    print('第三季度')
elif n==10 or n==11 or n==12:
    print('第四季度')
else:
    print('您输错了')

