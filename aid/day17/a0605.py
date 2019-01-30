#登录系统
name = input('请输入用户名：')
if name == '':
    name = 'admin'
pwss = input('请输入密码：')
#请登录
if name =='admin':
    if pwd =='123456':
        print('登录成功')
    else:
        print('密码输入有误！')
else:
    print('用户名输入有误！')
#结构s