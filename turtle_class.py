from turtle import Turtle,Screen
from turtle import *
import random as r
import turtle

class Paddle(Turtle):
    def __init__(self,xpos,ypos):
        self=Turtle("square")
        self.penup()
        self.setpos(xpos,ypos)
        self.turtlesize(2, 1, 0)
    def f(self,y):
        self.goto(self.pos()[0], y)
