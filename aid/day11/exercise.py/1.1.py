
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is int:
            s += x#如果是整数就加到
        else:
            s += sum_list(x)#如果是列表，把列表的加列表的和
    print('里面的s',s)
    return s






print(sum_list(L))