#模拟银行业务需求，用装饰器来扩展新功能
#银行:存钱,取钱









def privileged_chck(fn):
    def fx(n,x):
        print('权限认证中...')
        fn(n,x)
    return fx

def send_message(fn):
    '''实现业务操作完成后发送短消息的功能'''

    def fy(n,x):
        fn(n,x)#先操作，再发消息
        print('正在发消息给',n,'...')
    return fy



@privileged_chck
def savemoney(name,x):
    print(name,'存钱',x,'元')

@send_message
@privileged_chck
def withdraw(name,x):
    print(name,'取钱',x,'元')





savemoney('小王',200)
savemoney('小赵',400)

withdraw('小李',500)