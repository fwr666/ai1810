def fn_outer():
    #fn_outer  创建变量
    print("fn_outer　被调用了")
    def fn_inner():
        print('fn_inner 被调用了')
    fn_inner()
    fn_inner()
    print("fn_outer 调用结束")

fn_outer()