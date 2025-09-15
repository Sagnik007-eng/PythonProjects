"""class member:
    def __init__(self,name):
        self.name=name
        self.lib=self.librarian('Murty')

    def book_request(self):
        self.lib.book_issue(self.name)
    class librarian:
        def __init__(self,name):
            self.name=name
        def book_issue(self,n):
            print(self.name,'issued to',n)

m=member('Neha')
m.book_request()"""

from turtle import Turtle,Screen
from turtle import *
import random
import turtle
x=10
y=10
def up():
    global x
    x=x+5
    tim.goto(tim.pos()[0],x)

def dwn():
    global y
    y=y-5
    tim.goto(tim.pos()[0],y)

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
tim=Turtle("square")
tim.penup()
tim.setpos(-300,0)
tim.turtlesize(10,1,0)

screen.onkey(up,'u')
screen.onkey(dwn, 'd')
screen.listen()



screen.exitonclick()
