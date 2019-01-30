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