# 写一个函数 get_score()获取学生的成绩(0~100中的整数),
# 如果用户输入的成绩不是0~100之间的数，则返回0,
print('ss')
def get_score():
    s = input('请输入成绩(0~100)')

    try:
        score = int(s)
    except ValueError:
        return 0
    if 0 <= score <= 100:
        return score
    return 0
 
# try:
#     score=get_score()
    

# except:
#     score=0
# finally:
#     print(score)
print(get_score())


