#file_read.py

#此示例示意读取文件myfile.txt里的内容

try:
    myf = open('myfile.txt')
    print('打开文件成功')
    s = myf.read()
    print('读取%d个字符'%len(s),'内容是',s)
    myf.close()
except OSError:
    print('打开文件失败')

def read_info(filename):
    '''读取filename 内容,形成字典的列表返回
    返回:[
        {'name':'张三','age':20}
    ]