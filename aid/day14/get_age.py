

def get_age():
    age = int(input('请输入年龄'))
    if 1 <= age < 140:
        return age
    else:
        raise ValueError


try:
    age = get_age()
    print('用户输入的年龄是',age)
except ValueError as err:
    print('用户输入的不是1~140之间的整数')