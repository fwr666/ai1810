km = float(input('请输入公里数:'))

m = 13

if km >= 3:
    m = m + (km-3)*2.3
if km >= 15:
    m = m + 2.3*0.5*(km-15)
print(m)