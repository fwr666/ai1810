i = float(input("请输入第一个数："))
j = float(input("请输入第二个数："))
k = float(input("请输入第三个数："))

ma = i if i > j else j
ma = ma if ma > k else k
mi = i if i < j else j
mi = mi if mi < k else k
ave = (i + j + k)/3
print("最大值是:",ma)
print("最小值是:",mi)
print("平均值是:",ave)                                                        