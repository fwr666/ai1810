def test():
    x = 1
    print("test=",str(x))
    def test2():
        nonlocal x
        x = 3
        print("test2=",x)
    test2()
    print(x)
test()