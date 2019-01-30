#学生管理系统

#   4.改写之前的学生信息管理程序，将程序改为两个函数：
#        　　def input_student():
#              返回列表
#            def output_student(L):
#               打
         
#           测试（实现与之前相同的功能）:
#             infos = input_student()
#             output_student(infos)


infos = []#创建一个空的列表保存学生信息

#以下函数用于输入学生信息
def input_student():
    while True:
        d = {}
        name = input('请输入学生姓名：')
        if name == '':
            break
        age = int(input('请输入学生年龄:'))
        score = int(input('请输入学生成绩:'))
        
        d['name'] = name
        d['age'] = age
        d['score'] = score

        infos.append(d)

#以下函数用于输出学生信息
def output_student(infos):
    row = 20#　　　－　号的数量
    l = 18  #  中文空格数量
    print('+' + '-' * row +'+'+'-'*row+'+'+'-'*row+'+')
    print('|'+'姓名'.center(l)+'|'+'年龄'.center(l)+'|'+'成绩'.center(l)+'|')
    print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')

    #遍历列表中的字典，每个学生单独保存在一个字典中
    for d in infos:
        sn = d['name']
        sa = str(d['age'])
        ss = str(d['score'])

        count = 0
        for ch in sn:
            if int(0x4e00)<=ord(ch)<=int(0x9FA5):
                count += 1


        print('|%s|%s|%s|'%(sn.center(row-count),
                             sa.center(row),
                             ss.center(row)

        ))
    print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')

#删除学生信息
def delete_student():

    name = input('输入要删除的学生姓名')


    for i in range(len(infos)):
        d = infos[i]#此处是全局变量，如果删除了列表中的一个元素，还执行到这里会　越界！！！
        if d['name'] == name:
            del infos[i]
            return#删除了就退出
    print('木有这个学生')

#修改学生信息
def modify_student_score(L):
    name = input('请输入要修改的学生姓名')
    for d in L:
        if d['name'] == name:
            score = int(input('请输入学生成绩'))
            d['score'] = score
            return 

#成绩从高到低
def output_student_by_score_desc(L):
    L2 = sorted(L,key=lambda d:d['score'],reverse=True)
    output_student(L2)
#成绩从低到高
def putput_student_by_score_asc(L):
    L2 = sorted(L,key=lambda d:d['score'])
    output_student(L2)

def putput_student_by_age_desc(L):
    L2 = sorted(L,key=lambda d:d['age'],reverse=True)
    output_student(L2)

def age_lower_to_high(L):
    L2 = sorted(L,key=lambda d:d['age'])
    output_student(L2)






    # for i in range(len(L)):
    #     # d = L[i]
    #     if d['name'] == name:
    #         d['score'] = input('请输入要修改的新成绩')
    #         return
    # print('没有这个学生')



#以下函数用于显示菜单
def menu():
    print('+-------------------------+')
    print('| 1) 添加学生信息---------|')
    print('| 2) 显示学生信息---------|')
    print('| 3) 删除学生信息---------|')
    print('| 4) 修改学生成绩---------|')
    print('| 5) 按学生成绩高~低显示学生信息|')
    print('| 6) 按学生成绩低~高显示学生信息|')
    print('| 7) 按学生年龄高~低显示学生信息|')
    print('| 8) 按学生年龄低~高显示学生信息|')
    print('| q) 退出----------－-----|')
    print('+-------------------------+')

while True:
    menu()
    ch = input('请输入命令')
    if ch == '1':
        input_student()
    elif ch == '2':
        output_student(infos)
    elif ch == '3':
        delete_student()
    elif ch == '4':
        modify_student_score(infos)
    elif ch == '5':
        output_student_by_score_desc(infos)
    elif ch == '6':
        putput_student_by_score_asc(infos)
    elif ch == '7':
        putput_student_by_age_desc(infos)
    elif ch == '8':
        age_lower_to_high(infos)
    elif ch == 'q':
        break
    
    






# while True:
#     name = input('请输入姓名:')# 输入名字
#     if name == '':#当直接回车时结束输入 #if not n:
#         break
#     age = int(input('请输入年龄'))#添加年龄
#     score = float(input('请输入成绩'))#添加成绩
    
#     d = {}#每次循环开始都创建一个新的字典

#     d['name'] = name#ｄ字典添加名字
#     d['score'] = score
#     d['age'] = age 

#     infos.append(d)#把一个字典当做元素添加到学生信息列表中

# #以表格形式打印列表内容
# row = 20#　　　－　号的数量
# l = 18  #  中文空格数量
# print('+' + '-' * row +'+'+'-'*row+'+'+'-'*row+'+')
# print('|'+'姓名'.center(l)+'|'+'年龄'.center(l)+'|'+'成绩'.center(l)+'|')
# print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')

# #遍历列表中的字典，每个学生单独保存在一个字典中
# for d in infos:
#     print('|'+d['name'].center(row)+'|'+str(d['age']).center(row)+
#     '|'+str(d['score']).center(row)+'|')
# print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')
