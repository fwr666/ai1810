#turtle 海龟绘图 
import turtle#导入绘图工具
turtle.bgcolor('black')
cs =['red','yellow','blue','green']
turtle.speed(10)#设置速度

for x in range(400):
    turtle.forward(2*x)#向当前方绘图
    turtle.left(85)#转９０度
    turtle.color(cs[x%4])#切换颜色

turtle,mainloop()#显示