


#隐藏属性不会被　from import * 语句导入

def f():
    pass
def _f():
    pass
def __f():
    pass
name1 = 'aaa'
_name = 'bbb'
