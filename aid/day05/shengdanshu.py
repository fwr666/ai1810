#   3.输入一个整数，此整数代表树干的高度，打印一颗如下
#   形状的圣诞树
#   　如：
#   　　　输入　3　
#   　　　　打印如下：
#   　　 *
#      ***
#     *****
#       *
#       *
#       *

height = int(input('请输入树干高度'))

for blank in range(1,height+1):
    print(' '*(height-blank)+'*'*(2*blank-1))
for _ in range(height):
    print(' '*(height-1)+'*')