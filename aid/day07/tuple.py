# t = ()
# for x in range(1,10):
#     t += (x ** 2,)
#     print(t)

# t2 = tuple([x ** 2 for x in range(1,10)])
# print(t2)

# 写程序，将如下信息形成一个字典　seasons
#   '键'　　'值'
#   1     '春季有１,2,3月'
#   2      '夏季有4,5,6月'
#   3      '秋季有7,8,9月'
#   4       '冬季有10,11,12'

# 2　让用户输入一个整数代表这个季度，打印这个季度的信息，如果
# 　　用输入的信息不在字典内，则打印'信息不存在'

# seasons = {1:'春季有１,2,3月',2:'夏季有4,5,6月',3:'秋季有7,8,9月',4:'冬季有10,11,12'}
# print(seasons)
# num  = int(input("请输入季度信息"))
# if num in seasons:#在就打印信息，
#     print(seasons[num])
# else:
#     print('信息不存在')

# 练习：
# 　　输入一个字符串，打印出这个字符串出现过的字符及出现过的次数
# 　如：
# 　　请输入：abcdabcdaba
# 打印：
# 　　a:４次
# 　　b:3次
#     c:２次
#     d:1次
# d = {}
# s = 'abcdabcdaba'
# for key in s:
#     if key in d:
#         d[key] +=  1
#     else:
#         d[key] = 1
# print(d)

# for t in d.items():
#     print('%s:%d'%t) 


# s = input("qingshuru")
# d = {}
# for ch in s:
#     d[ch] = s.count(ch)
# O(n^2)
# words = {}
# while True:
#     s = input('请输入单词')
#     if s == ' ':#if not word
#         break
#     a = input('请输入这个单词的解释')
#     words[s] = a
# print("形成的字典是",words)
# while True:
#     s = input('请输入要查询的单词')
#     if s == '111':
#         print('告辞')
#         break
#     if s in words:
#         print(s,'--',words[s])
#     else:
#         print('没有此单词')

# 练习：
# 　有如下字符串列表：
# 　　L = ['abc','yingying','hello']
#     请生成如下字典：
#     　d = {'abc':6,'yingying':9,'hello':5}
# 　　　　注意　数字为字符串的长度

# L = ['abc','yingying','hello']#表达式可以用函数
# d = {x: len(x) for x in L}
# print(d)

# 练习二：
# 　　已知有两个等长的列表：
# 　　　　list1 = [1001,1003,1008,1004]
#        list2 = ['Tom','Jerry','Spike','Tyke']
#     用list1中的元素作为键，用list2中对应的元素作为值，生成如下字典：
list1 = [1001,1003,1008,1004]
list2 = ['Tom','Jerry','Spike','Tyke']
# d = {}
# for x in range(len(list2)):
#         d[list2[x]] = list1[x] 
#print(d)

d = {list2[i]:list1[i] for i in range(len(list1))}
print(d)