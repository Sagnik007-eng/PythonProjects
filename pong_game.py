from turtle import Turtle,Screen
#from turtle_class import *
from turtle import *
import random as r
import random as r1
import turtle
screen=Screen()
screen.title('Pong')
screen.setup(width=600,height=600)
tim=Turtle("circle")
tim.turtlesize(1)
s1=Turtle("square")
s1.penup()
s1.setpos(300,0)
s1.turtlesize(2,1,0)
x=10
y=10
point=0
def up():
    global x
    x=x+5

    s1.goto(s1.pos()[0],x)

def dwn():
    global y
    y=y-5

    s1.goto(s1.pos()[0],y)
tim.penup()
tim.speed(1)
while 1==1:
  tim.setpos(-300,0)
  tim.right(r.randint(30,50))
  tim.setpos(0,-300)
  tim.right(r.randint(30,70))
  y_pos=r1.randint(0,200)
  tim.setpos(300,y_pos)
  tim.left(r.randint(30,70))
  tim.setpos(0,-300)
  tim.left(r.randint(30,70))
  y_pos = r1.randint(0, 200)
  tim.setpos(-300,y_pos)
  if tim.xcor()==270 and s1.xcor()==290:
      tim.setpos(-300, 0)

      point=point+1
  screen.onkey(up, 'u')
  screen.onkey(dwn, 'd')
  screen.listen()


print(point)


screen.exitonclick()