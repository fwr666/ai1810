#此示例用于演示nonlocal
v = 100
def f1():
	v = 200
	print('f1.v=',v)
	def f2():
		nonlocal v #想让外部变量v 改变
		v = 300
		print('f2.v',v)
	f2()
	print('f1.v=',v)
f1()
print('v全局v=',v)
