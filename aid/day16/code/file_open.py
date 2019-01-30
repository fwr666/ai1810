

try:
    myfile = open("./myifle.txt")
    print('打开文件成功')
    myfile.close()
    print('关闭文件成功')
except:
    print('失败')
