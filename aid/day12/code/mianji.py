# #输入半径，打印圆的面积
# from math import pi,sqrt

# r = float(input('请输入圆的半径'))

# a = pi *  r ** 2
# print('圆的面积是',a)

# r = sqrt(a / (pi))
# print('圆的半径是',r)
import time
year = int(input('请输入出生年份'))
month = int(input('请输入出生月份'))
day = int(input('请输入出生日'))

birth_tuple = (year,month,day,0,0,0,0,0,0)
birth_second = time.mktime(birth_tuple)
life_second = time.time() - birth_second
life_day = life_second/60/60//24
print('您已出生',life_day,'天')
week = {
    0: '一',
    1: '二',
    2: '三',
    3: '四',
    4: '五',
    5: '六',
    6: '日'
}
birth_tuple = time.localtime(birth_second)
print('您出生的那天是星期',week[birth_tuple[6]])









