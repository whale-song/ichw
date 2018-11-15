# 作者：宋怀雨
# 化学与分子工程学院

# v1.3.3更新说明
# 增加了日期显示乌龟，同步协调运行日期显示。
# 修约日期显示小数为1，调整了日期刷新频率。解决了日期龟设置颜色失败的bug。
# 完成一周轨迹描画后各行星现在将不再描绘轨迹，提高了长时间运行情况下程序的运行速度和流畅性。
# 修复了年份显示错误的bug。

import turtle
import math as m

# 注册turtle
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
w = turtle.Turtle()

# 总运行数据组
# pa：半长轴
# pb：半短轴
# pc：1/2焦距
planet = [b, c, d, e, f, g]
pa = [58, 108, 150, 228, 389, 573]
pb = [56.7, 107, 150, 227, 388, 572]
pc = [11, 0.7, 2, 21, 19,32]
size = [0.5, 0.8, 1, 1.2, 3, 2.5]

# 参数初始化
turtle.bgcolor('black')
w.hideturtle()
j = 0

# Sun
a.speed(0)
a.hideturtle()
a.penup()
a.bk(25)
a.rt(90)
a.color('darkred','darkred')
a.pendown()
a.begin_fill()
a.circle(25)
a.end_fill()

# 行星初始化
b.color(175/255, 175/255, 175/255)
c.color(238/255, 201/255, 0/255)
d.color(32/255, 178/255, 170/255)
e.color(165/255, 42/255, 42/255)
f.color(255/255, 165/255, 0/255)
g.color(139/255, 69/255, 19/255)
w.color('white')

for i in range(6):
	planet[i].hideturtle()
	planet[i].turtlesize(size[i])
	planet[i].shape('circle')
	planet[i].speed(0)
	planet[i].penup()
	planet[i].fd( pa[i] + pc[i] )
	planet[i].pendown()
	planet[i].showturtle()
	planet[i].speed(9)

#planame = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn']

#for p in range(6):
#	def planame[p](i): #本行出错，需重新修改自变量
#		x = pa[p] * m.cos(3.14*i/180) + pc[p]
#		y = pb[p] * m.sin(3.14*i/180)
#		planet[p].goto(x,y)

# Mercury
# a=58000000, b=56700000, e=0.205630, c=11926540
# T=87.9d
def mercury(i):
    x=58 * m.cos(3.14*i/180)+11
    y=56.7 * m.sin(3.14*i/180)
    b.goto(x,y)
    if i >= 360:
    	b.penup()

# Venus
# a=108208000, b=108206759, e=0.006772, c=732784
# T=224.7d
def venus(i):
    x=108 * m.cos(3.14*i/180)+0.7
    y=107 * m.sin(3.14*i/180)
    c.goto(x,y)
    if i >= 360:
    	c.penup()

# Earth
# a=149598023, b=14957580, e=0.0167086, c=2499573
# T=365d	
def earth(i):
    x=150 * m.cos(3.14*i/180)+2
    y=150 * m.sin(3.14*i/180)
    d.goto(x,y)
    if i >= 360:
    	d.penup()

# Mars
# a=227939200, b=227440455, e=0.0934, c=212895214
# T=693.5d
def mars(i):
    x=228 * m.cos(3.14*i/180)+21
    y=227 * m.sin(3.14*i/180)
    e.goto(x,y)
    if i >= 360:
    	e.penup()

# Jupiter
# (该行星轨道距太阳过远，已按0.5倍比例缩放其轨道)
# a=778570000, b=777638580, e=0.0489, c=38072073
# T=4309d
def jupiter(i):
    x= 389 * m.cos(3.14*i/180)+19
    y= 388 * m.sin(3.14*i/180)
    f.goto(x,y)
    if i >= 360:
    	f.penup()

# Saturn
# (该行星轨道距太阳过远，已按0.4倍例缩放其轨道)
# a=1433530000, b=1431240078, e=0.0565, c=80994445
# T=10767d
def saturn(i):
    x=573 * m.cos(3.14*i/180)+32
    y=572 * m.sin(3.14*i/180)
    g.goto(x,y)
    if i >= 360:
    	g.penup()

# Date
# 1 degree = (87.9/360)d
def date(i):
	x = -(int(m.log10(int(i)+1)) * 9 + 20)
	y = -265 
	w.clear()
	w.speed(0)
	w.penup()
	w.goto(x, y)
	w.pendown()
	w.write(str('%.1f' % i) + "year", font=("Arial", 12, "bold"))


if __name__ == '__main__':
	while True:
		for n in range(360*122):
			if n%155 == 0:
				date(j)

			if n%6 == 0:
				mercury(n)
			elif n%6 == 1:
				venus(48*n/122)
			elif n%6 == 2:
				earth(29*n/122)
				j += (168.6/43920)
			elif n%6 == 3:
				mars(15*n/122)
			elif n%6 == 4:
				jupiter(3*n/122)
			else:
				saturn(n/122)


