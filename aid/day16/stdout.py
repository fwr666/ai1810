import sys
# sys.stdout.write('hello world')
# sys.stderr.write('错误啊')
f = open("myprint.txt",'w')
print(1,2,3,4,5,file = f)
f.close()
print('程序正常退出')