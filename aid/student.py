#学生管理系统

infos = []#创建一个空的列表保存学生信息
while True:
    name = input('请输入姓名:')# 输入名字
    if name == '':#当直接回车时结束输入 #if not n:
        break
    age = int(input('请输入年龄'))#添加年龄
    score = float(input('请输入成绩'))#添加成绩
    
    d = {}#每次循环开始都创建一个新的字典

    d['name'] = name#ｄ字典添加名字
    d['score'] = score
    d['age'] = age 

    infos.append(d)#把一个字典当做元素添加到学生信息列表中

#以表格形式打印列表内容
row = 20#　　　－　号的数量
l = 18  #  中文空格数量
print('+' + '-' * row +'+'+'-'*row+'+'+'-'*row+'+')
print('|'+'姓名'.center(l)+'|'+'年龄'.center(l)+'|'+'成绩'.center(l)+'|')
print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')

#遍历列表中的字典，每个学生单独保存在一个字典中
for d in infos:
    print('|'+d['name'].center(row)+'|'+str(d['age']).center(row)+
    '|'+str(d['score']).center(row)+'|')
print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')







