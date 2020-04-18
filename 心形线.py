#PythonDraw.py
import turtle 
import math

#界面初始化
turtle.setup(960,680,200,100)
turtle.bgcolor("black")
#创建两只turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t.hideturtle()
t1.hideturtle()

#绘制x,y轴
t.pensize(3)
t.pencolor("green")
t.speed(5)
#绘制x轴
t.pu()
t.goto(-300,0)
t.pendown()
t.goto(300,0)
t.goto(295,5)
t.penup()
t.goto(300,0)
t.pendown()
t.goto(295,-5)
#绘制y轴
t.penup()
t.goto(0,-300)
t.pendown()
t.goto(0,300)
t.goto(-5,295)
t.penup()
t.goto(0,300)
t.pendown()
t.goto(5,295)

#画笔初始化
def Init():
      t1.speed(10)
      t1.penup()
      t1.goto(0,0)
      t1.pendown()
      t1.pensize(3)

#1
def move1():
      t1.pencolor("red")
      t1.penup()
      t1.goto(240,270)
      t1.down()
      t1.write("ρ=a*(1-sinθ)",font =("Arial",28," normal"))
      t1.penup()
      t1.goto(0,0)
      t1.pendown()
      angle = 90
      Init()
      while angle <= 540:
            a = 100*(1-math.sin(math.radians(angle)))
            x = a*math.cos(math.radians(angle))
            y = a*math.sin(math.radians(angle))
            t1.goto(x,y)
            angle = angle + 0.5

#2
def move2():
      t1.pencolor("red")
      t1.penup()
      t1.goto(240,270)
      t1.down()
      t1.write("ρ=a*(1+sinθ)",font =("Arial",28," normal"))
      t1.penup()
      t1.goto(0,0)
      t1.pendown()
      angle = -90
      Init()
      while angle <= 360:
            t1.pencolor("red")
            a = 100*(1+math.sin(math.radians(angle)))
            x = a*math.cos(math.radians(angle))
            y = a*math.sin(math.radians(angle))
            t1.goto(x,y)
            angle = angle + 0.5

#3
def move3():
      t1.pencolor("red")
      t1.penup()
      t1.goto(240,270)
      t1.down()
      t1.write("ρ=a*(1-cosθ)",font =("Arial",28," normal"))
      t1.penup()
      t1.goto(0,0)
      t1.pendown()
      angle = 0
      Init()
      while angle <= 450:
            t1.pencolor("red")
            a = 100*(1-math.cos(math.radians(angle)))
            x = a*math.cos(math.radians(angle))
            y = a*math.sin(math.radians(angle))
            t1.goto(x,y)
            angle = angle + 0.5

#4
def move4():
      t1.pencolor("red")
      t1.penup()
      t1.goto(240,270)
      t1.down()
      t1.write("ρ=a*(1+cosθ)",font =("Arial",28," normal"))
      t1.penup()
      t1.goto(0,0)
      t1.pendown()
      angle = 180
      Init()
      while angle <= 630:
            t1.pencolor("red")
            a = 100*(1+math.cos(math.radians(angle)))
            x = a*math.cos(math.radians(angle))
            y = a*math.sin(math.radians(angle))
            t1.goto(x,y)
            angle = angle + 0.5

#5
def move5():
      Init()
      turtle.bgpic("2.1.png")
      t1.penup()
      t1.goto(240,270)
      t1.down()
      t1.pu()
      t1.goto(0,150*(math.pi/2.0-1))
      t1.pd()

      x = -0.009
      while x > -1:
            t1.pencolor("red")
            y = math.sqrt(1/4.0-pow(x+0.5,2))+math.pi/2-1
            t1.goto(150*x,150*y)
            x = x - 0.001

      x = -1
      while x <= 1:
            t1.pencolor("red")
            y = -math.tan(math.sqrt(1-pow(abs(x),1.5)))+math.pi/2-1
            t1.goto(150*x,150*y)
            x = x + 0.001

      x = 1
      while x >= 0:
            t1.pencolor("red")
            y = math.sqrt(1/4.0-pow(x-0.5,2))+math.pi/2-1
            t1.goto(150*x,150*y)
            x = x - 0.001

#6
def move6():
      Init()
      turtle.bgpic("3.1.png")
      t1.pu()
      t1.goto(0,100)
      t1.pd()
      t1.pencolor("red")
      x = 0
      while x <= 1:
            y = math.sqrt(1-x*x)+pow(x,2.0/3)
            t1.goto(100*x,100*y)
            x += 0.001
      x = 1
      while x >= -1:
            y = -math.sqrt(1-x*x)+pow(x*x,1.0/3)
            t1.goto(100*x,100*y)
            x -= 0.001
      x = -1
      while x <= 0:
            y = math.sqrt(1-x*x)+pow(x*x,1.0/3)
            t1.goto(100*x,100*y)
            x += 0.001

#7
def move7():
      Init()
      turtle.bgpic("4.1.png")
      t1.pu()
      t1.goto(-60*math.sqrt(10),36*math.sqrt(10))
      t1.pd()
      t1.pencolor("red")
      x = -2*math.sqrt(10)
      while x <= 2*math.sqrt(10):
            y = (3*abs(x)+4*math.sqrt(abs(40-x*x)))/5.0
            t1.goto(30*x,30*y)
            x += 0.001
            
      x = 2*math.sqrt(10)
      while x >= -2*math.sqrt(10):
            y = (3*abs(x)-4*math.sqrt(abs(40-x*x)))/5.0
            t1.goto(30*x,30*y)
            x -= 0.001

#8
def move8():
      Init()
      turtle.bgpic("5.1.png")
      t1.pu()
      x = -1.13902 #最左端
      t1.goto(-113.902,(pow(x*x,1.0/3)+pow((pow(pow(x,4),1.0/3)-4*x*x+4),0.5))*50)
      t1.pd()
      t1.pencolor("red")
      x = -1.13902
      while x <= 1.13902:
            y =  (pow(x*x,1.0/3)+pow((pow(pow(x,4),1.0/3)-4*x*x+4),0.5))/2.0
            t1.goto(100*x,100*y)
            x += 0.001

      x = 1.13902
      while x >= -1.13902:
            y =  (pow(x*x,1.0/3)-pow((pow(pow(x,4),1.0/3)-4*x*x+4),0.5))/2.0
            t1.goto(100*x,100*y)
            x -= 0.001

#9
def move9():
      Init()
      turtle.bgpic("6.1.png")
      t1.pu()
      x = -1.139
      t1.goto(-113.9,(pow(x*x,1/3.0)+math.sqrt(pow(pow(x,4),1/3.0)-4*x*x+4))*50.0)
      t1.pd()
      t1.pencolor("red")
      x = -1.139
      while x <= 1.139:
            y = (pow(x*x,1/3.0)+math.sqrt(pow(pow(x,4),1/3.0)-4*x*x+4))/2.0
            t1.goto(x*100,y*100)
            x += 0.001
      x = 1.139
      while x >= -1.139:
            y = (pow(x*x,1/3.0)-math.sqrt(pow(pow(x,4),1/3.0)-4*x*x+4))/2.0
            t1.goto(x*100,y*100)
            x -= 0.001

#10
def move10():
      Init()
      turtle.bgpic("7.1.png")
      t1.pu()
      t1.goto(-160,0)
      t1.pd()
      t1.speed(10)
      t1.pencolor("red")
      x = -2
      while x <= 2:
            y = math.sqrt(1-pow(abs(x)-1,2))
            t1.goto(x*80,y*80)
            x += 0.001
      x = 2
      while x >= -2:
            y = -3*math.sqrt(1-math.sqrt(abs(x)/2.0))
            t1.goto(x*80,y*80)
            x -= 0.001

#11
def move11():
      Init()
      turtle.bgpic("8.1.png")
      t1.pencolor("red")
      angel = 0
      t1.pu()
      t1.goto(120,0)
      t1.pd()
      while angel <= 360:
            a = math.sin(math.radians(angel))*math.sqrt(abs(math.cos(math.radians(angel))))\
                /(math.sin(math.radians(angel))+7.0/5)-2*math.sin(math.radians(angel))+2
            x = a*math.cos(math.radians(angel))
            y = a*math.sin(math.radians(angel))
            t1.goto(x*60,y*60)
            angel += 0.1

#12
def move12():
      Init()
      turtle.bgpic("9.1.png")
      t1.pencolor("red")
      t1.pu()
      t1.goto(-200,0)
      t1.pd()
      x = -2
      while x <= 2:
            y = math.sqrt(2*abs(x)-x*x)
            t1.goto(x*100,y*100)
            x += 0.001
      x = 2
      while x >= -2:
            y = -2.14*math.sqrt(math.sqrt(2)-math.sqrt(abs(x)))
            t1.goto(x*100,y*100)
            x -= 0.001

#13
def move13():
      Init()
      turtle.bgpic("10.1.png")
      t1.pencolor("red")
      t1.pu()
      t1.goto(-100,58)
      t1.pd()
      x = -1
      while x <= 1:
            y = math.sqrt((1-x*x)/2.0)+3/5.0*pow(x*x,1/3.0)
            t1.goto(x*100,y*100)
            x += 0.001
      x = 1
      while x >= -1:
            y =-math.sqrt((1-x*x)/2.0)+3/5.0*pow(x*x,1/3.0)
            t1.goto(x*100,y*100)
            x -= 0.001

#14
def move14():
      Init()
      turtle.bgpic("11.1.png")
      t1.pencolor("red")
      t1.pu()
      t1.goto(0,0)
      t1.pd()
      angle = -math.pi
      while angle <= -math.pi/2:
            a = 5*pow(math.sin(angle),7)*math.exp(abs(2*angle))
            x = a*math.cos(angle)
            y = a*math.sin(angle)
            t1.goto(x*1.5,y*1.5)
            angle += 0.001
      angle = math.pi/2
      while angle <= math.pi:
            a = 5*pow(math.sin(angle),7)*math.exp(abs(2*angle))
            x = a*math.cos(angle)
            y = a*math.sin(angle)
            t1.goto(x*1.5,y*1.5)
            angle += 0.001

#15
def move15():
      Init()
      turtle.bgpic("12.1.png")
      t1.pencolor("red")
      t1.pu()
      t1.goto(0,50)
      t1.pd()
      angle = 0
      while angle <= 2*math.pi:
            x = 16*pow(math.sin(angle),3)
            y = 13*math.cos(angle)-5*math.cos(2*angle)-2*math.cos(3*angle)\
                -math.cos(4*angle)
            t1.goto(x*10,y*10)
            angle += 0.001

#程序开始
turtle.ontimer(move1(),2000)  
t1.clear()
turtle.ontimer(move2(),2000)
t1.clear()
turtle.ontimer(move3(),2000)
t1.clear()
turtle.ontimer(move4(),2000)
t1.clear()
turtle.ontimer(move5(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move6(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move7(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move8(),2000)
t1.clear()
turtle.bgpic("nopic")                        
turtle.ontimer(move9(),2000)
t1.clear()
turtle.bgpic("nopic")                        
turtle.ontimer(move10(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move11(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move12(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move13(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move14(),2000)
t1.clear()
turtle.bgpic("nopic")
turtle.ontimer(move15(),2000)
t1.clear()
turtle.bgpic("nopic")  

#结束
t.clear()
turtle.done()
