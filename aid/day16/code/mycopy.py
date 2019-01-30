# 练习:
#   1. 写程序实现复制文件的功能
#     要求:
#        1. 要考虑特大文件问题
#        2. 要关闭文件
#        3. 要能复制二进制文件
#     如:
#       请输入源文件路径名:  /home/tarena/xxx.tar.gz
#       请输入目标文件路径名: ./a.tar.gz
#     显示:
#       文件已成功复制

# scr_filename = input("请输入源文件路径")
# dst_filename = input("请输入目标文件路径")


# try:
#     scr = open(scr_filename,"rb")
#     try:
#         try:
#             dst = open(dst_filename,"wb")
#             try:
#                 while True:
#                     b = scr.read(4096)
#                     if not b:
#                         break
#                     dst.write(b)
#                     print("复制成功")
#             finally:
#                 dst.close()
#         except OSError:
#             print("打开写文件失败")
#     finally:
#         scr.close()
# except OSError:
#     print("复制失败")

#
def copy(src_file,dst_file):
    ''' src_file:源文件名
        dst_filr:目标文件名
        返回值：True成功，False 失败
    '''
    fr = open(src_file,'rb')
    fw = open(dst_file,'wb')
    try:
        while True:
            b = fr.read(4096)
            if not b:
                break
            fw.write(b)
        fr.close()
        fw.close()
    except OSError:
        return False
    return True
src = input("请输入源文件名：")
dst = input('请输入目标文件名:')




 