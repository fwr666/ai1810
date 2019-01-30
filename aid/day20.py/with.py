fr = open("test.txt",'r')
for line in fr:
    try:
        print(line)
        3/0
    finally:
        fr.close()
except OSError:
    print('文件打开失败')
