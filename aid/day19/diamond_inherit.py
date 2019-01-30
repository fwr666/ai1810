#diamond_inherit.py

class A:
    def go(self):
        print('A')

class B(A):
    def go(self):
        print('A')
class C(A):
    def go(self):
        print('C')
class D(B,C):
    def go(self):
        print('D')
d = D()
d.go()

对象转字符串函数的使用：
　　repr(x) 返回一个符合python语法规则且能代表此对象的表达式字符串
         通常：
         　　eval(repr(obj)) == obj 为True

    str(x) 返回一个代表对象的字符串（这个字符串通常是给我阅读的)

    示例：
    　s = "I'm a five"
    sr = repr(s)
    ss = str(s)
    print(sr)
    print(ss)