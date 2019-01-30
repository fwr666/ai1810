def div_apple(n):
    print('%d个苹果您想分给几个人'%n)
    s = input('请输入人数')
    count = int(s)
    result = n / count
    print('每一个分了',result,'个苹果')

try:
    div_apple(10)
    print('分苹果成功')
except ValueError:   #err 绑定错误对象
    print('失败,错误信息err=')
except:
    print('除ValueError外的错误发生了')
else:
    print('没有发生异常,nice')
finally:
    print('最终语句，此语句在离开try 时一定会被执行')

print('程序正常结束')