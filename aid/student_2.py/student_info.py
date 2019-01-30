
from student import *

#此函数用于输入学生信息
def input_student():
    L = []#空列表用于存储学生信息

    while True:
        name = input('请输入学生姓名:')
        if name == '':
            break
        try:
            age = int(input('请输入学生年龄:'))
            score = float(input('请输入学生成绩:'))
        except ValueError:
            print('输入年龄或成绩有误，请重新输入!')
        d = Student(name,age,score)
        L.append(d)
    print(L)

    return L

#以下函数用于输出学生信息
def output_student(infos):

    row = 20#　　　－　号的数量
    l = 18  #  中文空格数量
    print('+' + '-' * row +'+'+'-'*row+'+'+'-'*row+'+')
    print('|'+'姓名'.center(l)+'|'+'年龄'.center(l)+'|'+'成绩'.center(l)+'|')
    print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')

    #遍历列表中的字典，每个学生单独保存在一个字典中
    for s in infos:
        sn,sa,ss = s.get_info()
        count = 0#统计中文个数，用于对齐格式
        for ch in sn:
            if int(0x4e00)<=ord(ch)<=int(0x9FA5):
                count += 1


        print('|%s|%s|%s|'%(sn.center(row-count),
                             str(sa).center(row),
                             str(ss).center(row)

        ))
    print('+'+'-'*row+'+'+'-'*row+'+'+'-'*row+'+')


def delete_student(info):

    name = input('输入要删除的学生姓名')


    for i in len(info):
        d = info[i].get_name()#获取学生名字
        if d == name:
            del info[i]#删除学生对象
            return info#删除了就退出
    print('木有这个学生')
    return info

#修改学生信息
def modify_student_score(L):
    name = input('请输入要修改的学生姓名')
    for d in L:
        if d.get_name() == name:
            try:
                score = float(input('请输入学生成绩'))
                d.score = score
            except ValueError:
                print('输入的成绩不合法')
            return L
    return L

def output_student_by_score_desc(L):
    L2 = sorted(L,key=lambda d:d.get_score(),reverse=True)
    output_student(L2)

#成绩从低到高
def putput_student_by_score_asc(L):
    L2 = sorted(L,key=lambda d:d.get_score())
    output_student(L2)

def putput_student_by_age_desc(L):
    L2 = sorted(L,key=lambda d:d.get_age(),reverse=True)
    output_student(L2)

def age_lower_to_high(L):
    L2 = sorted(L,key=lambda d:d.get_age())
    output_student(L2)
        
# #函数作用：存储学生信息,文件名为(si.txt)
# def save_file(infos):
#     five = open("si.txt",'r+')
#     for d in infos:
#         five.write(d['name']+' '+str(d['age'])\
#         +' '+str(d['score'])+'\n')
#     print("保存成功")
#     five.close()
#     five = open("si.txt",'r')
#     b =five.read()
#     print(b)
#     five.close()


#函数作用：从文件中读取学生信息,文件名为(si.txt)
# def read_file():
#     L = []
#     try:
#         five = open("si.txt",'rt')
#         while True:
#             s = five.readline()
#             if not s:
#                 break
#             s2 = s.rstrip()
#             n,a,s = s2.split()
#             a = int(a)
#             s = int(s)
#             L.append(dict(name=n,age=a,score=s))
#     except OSError():
#         print("读取数据失败")
       
#     finally:
#         five.close()
#     return L
#     output_student(L)#显示信息 

    #函数作用：存储学生信息,文件名为(si.txt)
def save_file(infos):
    five = open("si.txt",'r+')
    for d in infos:
        d.write_to(five)

    print("保存成功")
    five.close()
    five = open("si.txt",'r')
    b =five.read()
    print(b)
    five.close()

#函数作用：从文件中读取学生信息,文件名为(si.txt)
def read_file():
    L = []
    try:
        five = open("si.txt",'rt')
        while True:
            s = five.readline()
            if not s:
                break
            s2 = s.rstrip()
            n,a,s = s2.split(',')
            a = int(a)
            s = float(s)
            L.append(Student(n,a,s))
    except OSError():
        print("读取数据失败")
       
    finally:
        five.close()
    return L
    output_student(L)#显示信息 
