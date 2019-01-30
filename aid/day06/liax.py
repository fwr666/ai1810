# #输入一些正整数
# 存入列表Ｌ中，当输入－１时结束输入
# １．打印出列表中存有的数字
# ２．打印出您输入的数字的最大数
# ３．打印出您输入的这些数的平均数
# L = []
# while True:
#     num = int(input("请输入一些数"))
#     if num == -1:
#         break
#     # L[-1:-1:] = [num]
#    
#     L.append(num)
# for x in L:
#     print(x)
# print('你输入这些数中最大的是',max(L))
# print(sum(L)/len(L))


# L = []
# while True:
#     num = int(input("请输入两个以上数字"))
#     if num not in L:
#         L.append(num)
#     if num < 0:
#         break
# print(sum(L))
# print(L)
# L.sort()
# print(L[-1])
# print(L[-2])
# L[::] = L[1:]
# print(L)
# L = []
# while True:
#     x = int(input("请输入正整数:"))
#     if x < 0:#此处再次判断，查看已经获取的整数
#         if len(L) > 2:
#             break
#         else:
#             print("您输入的数字太少，请继续输入")
#     if x in L:#if L.count(x) !=0:  #判断x是否是输入过的数字
#         print("您已经输入过这个数字了，请输入其他的数")
#     else:
#         L.append(x)
        
    
# print(L)
# L2 = L.copy()
# L2.sort()#从小到大排序
# print("最大的数是",L2[-1])
# print('第二大的数是',L2[-2])
# print("这些数的和是：",sum(L))
# print("最大的一个数是：",max(L))
# #方法一　先删除最大的数，剩下的就是最大的数
# L.remove(max(L))
# a=[x for x in range(1,100,2)]  
# print(a)

L = [x+y for x in "ABC" for y in "123"]
print(L)