def fun(**kwargs):
    print("关键字传参个数是", len(kwargs))
    print('kwargs=', **kwargs)


fun(a=1, b="BBBB", c=66)  # 关键字传参
# fun()
fun(a=1, b=2, c=3, d=4)