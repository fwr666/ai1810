


d = {}
while True:
    print('1) 添加单词')
    print('2) 删除单词')
    print('3) 查找单词')
    print('q) 退出')
    ch = input('请输入命令')
    
    if ch == '1':
        key = input('请输入单词')
        value = input('请输入单词解释')
        if key in d:
            print('单词已存在')
        else:
            d[c] = s
    if ch == '2':
        c = input('输入要删除的单词')
        if c in d:
            del d[c]
        else:print('没有这个单词')
    if ch == '3':
        c = input('请输入要查找的单词')
        if c in d:
            print(d[c])
        else:print('没有这个单词')
    if ch == 'q':
        break











