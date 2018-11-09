import turtle
import math as m

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()

#Sun
a.speed(0)
a.hideturtle()
a.penup()
a.bk(25)
a.rt(90)
a.color('red','red')
a.pendown()
a.begin_fill()
a.circle(25)
a.end_fill()

#Mercury
#a=58000000, b=56700000, e=0.205630, c=11926540
#T=87.9d
b.color(175/255, 175/255, 175/255)
b.turtlesize(0.5)
b.hideturtle()
b.shape('circle')
b.speed(0)
b.penup()
b.fd(58+11)
b.pendown()
b.showturtle()
b.speed(9.9)
def mercury(i):
    x=58 * m.cos(3.14*i/180)+11
    y=56.7 * m.sin(3.14*i/180)
    b.goto(x,y)
    
#Venus
#a=108208000, b=108206759, e=0.006772, c=732784
#T=224.7d
c.color(238/255, 201/255, 0/255)
c.turtlesize(0.8)
c.hideturtle()
c.shape('circle')
c.speed(0)
c.penup()
c.fd(108+0.7)
c.pendown()
c.showturtle()
c.speed(9.8)
def venus(i):
    x=108 * m.cos(3.14*i/180)+0.7
    y=107 * m.sin(3.14*i/180)
    c.goto(x,y)

#Earth
#a=149598023, b=14957580, e=0.0167086, c=2499573
#T=365d
d.color(32/255, 178/255, 170/255)
d.turtlesize(1)
d.hideturtle()
d.shape('circle')
d.speed(0)
d.penup()
d.fd(150+2)
d.pendown()
d.showturtle()
d.speed(9.5)
def earth(i):
    x=150 * m.cos(3.14*i/180)+2
    y=150 * m.sin(3.14*i/180)
    d.goto(x,y)
    

#Mars
#a=227939200, b=227440455, e=0.0934, c=212895214
#T=693.5d
e.color(165/255, 42/255, 42/255)
e.turtlesize(1.2)
e.hideturtle()
e.shape('circle')
e.speed(0)
e.penup()
e.fd(228+21)
e.pendown()
e.showturtle()
e.speed(9)
def mars(i):
    x=228 * m.cos(3.14*i/180)+21
    y=227 * m.sin(3.14*i/180)
    e.goto(x,y)

#Jupiter
#(该行星轨道距太阳过远，已按0.5倍比例缩放其轨道)
#a=778570000, b=777638580, e=0.0489, c=38072073
#T=4309d
f.color(255/255, 165/255, 0/255)
f.turtlesize(3)
f.hideturtle()
f.shape('circle')
f.speed(0)
f.penup()
f.fd(389+19)
f.pendown()
f.showturtle()
f.speed(1)
def jupiter(i):
    x= 389 * m.cos(3.14*i/180)+19
    y= 388 * m.sin(3.14*i/180)
    f.goto(x,y)

#Saturn
#(该行星轨道距太阳过远，已按04倍例缩放其轨道)
#a=1433530000, b=1431240078, e=0.0565, c=80994445
#T=10767d
g.color(139/255, 69/255, 19/255)
g.turtlesize(2.5)
g.hideturtle()
g.shape('circle')
g.speed(0)
g.penup()
g.fd(605.8)
g.pendown()
g.showturtle()
g.speed(1)
def saturn(i):
    x=573 * m.cos(3.14*i/180)+32
    y=572 * m.sin(3.14*i/180)
    g.goto(x,y)


if __name__ == '__main__':
	while True:
		for n in range(360*6):
			x1 = int(n/6)
			if n%6 == 0:
				for p in range(122*x1, 122*(1+x1)):
					mercury(p)
			elif n%6 == 1:
				for p in range(48*x1, 48*(x1+1)):
					venus(p)
			elif n%6 == 2:
				for p in range(29*x1, 29*(x1+1)):
					earth(p)
			elif n%6 == 3:
				for p in range(15*x1, 15*(x1+1)):
					mars(p)
			elif n%6 == 4:
				for p in range(3*x1, 3*(x1+1)):
					jupiter(p)
			else:
				saturn(x1)


