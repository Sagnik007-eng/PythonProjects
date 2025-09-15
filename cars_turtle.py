from turtle import Turtle,Screen
#from turtle_class import *
from turtle import *
import random as r
import random as r1
import turtle
screen=Screen()
screen.title('Cars')
screen.setup(width=700,height=700)
point=0
class Car(Turtle):
    def __init__(self,x,y,rad,col):
        super().__init__()
        self.penup()
        self.color(col)
        self.shape("square")
        self.setheading(rad)
        self.setpos(x,y)
    def fwd(self):
        #while self.xcor()!= -350:
        self.forward(1)

    def setposition(self):
        self.setpos(350,r.randint(-300,338))

    def start_pos(self):
        self.goto(20,-350)

    def pt(self):
        global point
        point=point+1
        print(point)




s1=Car(170,-350,90,'black')
x=10
y=10
x1=10
y1=10
def up():
    global x
    x=x+5
    s1.goto(s1.pos()[0],x)

def dwn():
    global y
    y=y-5
    s1.goto(s1.pos()[0],y)

def rgt():
    global x1
    x1=x1+5
    s1.goto(x1,s1.pos()[1])

def lft():
    global y1
    y1=y1-5
    s1.goto(y1,s1.pos()[1])

trtls=int(input("Enter number of turtles"))
list_turtles=[]
for i in range(0,trtls):
    t=Car(350,r.randint(-300,338),180,'red')
    list_turtles.append(t)

game_is_on=True
while game_is_on:
    for i in list_turtles:
        i.fwd()
        screen.onkey(up, 'Up')
        screen.onkey(dwn, "Down")
        screen.onkey(lft, 'Left')
        screen.onkey(rgt, "Right")
        screen.listen()
        if i.xcor()==-350:
            i.setposition()
        if s1.xcor()==i.xcor()+20:
            if i.ycor() in range(s1.ycor()-20,s1.ycor()+20):
                game_is_on=False
        if s1.ycor()>=350:
            s1.start_pos()
            s1.pt()







screen.exitonclick()