#此示例示意用文件流对象的ｓｅｅｋ方法来移动文件的读写指针位置
try:
    fr = open("byte20.txt",'rb')
    b = fr.read(2)
    print(b)
    fr.seek(5,0)
    b = fr.read(5)
    print('移动后',b)
    fr.close()
except:
    print('打开失败')