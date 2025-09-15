from turtle import Turtle,Screen
from turtle_class import *
from turtle import *
import pandas as p
screen=Screen()
t=Turtle()
t.penup()
screen.bgpic("blank_states_img.gif")
state_dict={}
df=p.read_csv('50_states.csv')
#print(df[df['state']=='Alabama']['x'])
state_list=list(df['state'])
#state_x=list(df['x'])
#state_y=list(df['y'])

for i in state_list:
    state_dict[i]=[int(df[df['state']==i]['x']),int(df[df['state']==i]['y'])] #Creating a dictionary containing State as Key and (x,y) as vale

while True:
    state=screen.textinput('Enter State', 'US')
    t.setpos(state_dict[state][0],state_dict[state][1])
    t.write(state,True,align="center")






screen.exitonclick()