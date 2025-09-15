from turtle import Turtle,Screen
from turtle import *
import random
import turtle
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

class Snake():
    def __init__(self,l,score):
        self.l=l
        self.score=score
    def rgt(self):
        self.rt(90)
    def lft(self):
        self.left(90)
    def fun(self):
        tim=Turtle("square")
        tim.penup()
        tim.color("white")
        tim.shapesize(1,self.l)
        food=Turtle("circle")
        food.color("white")
        food.turtlesize(0.1,0.1,0)
        food.penup()
        t=Turtle()
        t.hideturtle()
        t.shapesize(1,4)
        t.setpos(0,300)
        t.color("white")
        t.penup()


        def rgt():
            tim.rt(90)
        def lft():
            tim.left(90)
        while (abs(list(tim.pos())[0])<300):
          x=random.randint(0,50)
          y=random.randint(0,60)
          if (abs(list(tim.pos())[1])==300):
              print("U hv hit the wall!!..U loose!!")
              break
          if (abs(list(tim.pos())[0])==300):
              print("U hv hit the wall!!..U loose!!")
              break
          tim.forward(random.randint(0,1))
          if (abs(list(tim.pos())[0])==abs(list(food.pos())[0])):
              #if ((abs(list(tim.pos())[1]) - abs(list(food.pos())[1])))<0.3:
                  food.setpos(x,y)
                  self.l=self.l+1
                  tim.shapesize(1,self.l)
                  self.score+=1
                  t.clear()
                  t.write(f"Score:{self.score}", True, align="center", font=("Arial", 24, "normal"))


          screen.onkey(rgt,'r')
          screen.onkey(lft, 'l')
          screen.listen()
        #print(f'Score is {self.score}')



s1=Snake(1,0)
s1.fun()

#print(s1.score)
screen.exitonclick()