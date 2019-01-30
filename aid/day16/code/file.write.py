
#此文件示意打开一个文本文件，并向里面写入内容

try:
    fw = open("mynote.txt",'+')#创建文件并写
    fw.write('hello')
    fw.write('world')
    
    fw.close()
    print('写入成功')
except OSError:
    print('打开文件失败')