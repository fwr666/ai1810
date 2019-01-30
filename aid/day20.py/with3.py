class A:
    def __enter__(self):
        print('A.__enter__被调用')
        self.file = open('test.txt')
        return self
    def __exit__(self,e_type,e_value,e_cb):
        self.file.close()
        if e_type is None:
            print('程序正常退出')
        else:
            print('离开with语句时发生异常')
            print('异常类型是',e_type)
            print('值是',e_value)
            print('追踪对象是',e_cb)
        print('A.__exit__被调用，已离开with语句')


    
with A() as a:
    a.file.redline()
    print('这是内部')

print("程序正常退出")