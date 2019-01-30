def make_except():
    print('开始...')
    print('结束...')
    # raise ZeroDivisionError#触发ValueError 异常#raise 类型
    #创建一个错误对象用error来绑定
    error = ValueError("xxx")
    raise error    #触发ValueError 类型的错误对象
    print('哈哈')


try:
    make_except()

    print('make_except 调用完成')
except ValueError as err:    #err 用来绑定raise发出的错误对象
    print('收到ValueError类型的错误通知',err)
# # except ZeroDivisionError:
# #     print('0')

# print('程序正常结束')
# make_except()