#In progress

from turtle import *

##Assign variables.
#c = 67
#b = 0

#Move the turtle to the starting position.
penup()
goto(-100, 70)
pendown()

#Set the turtle speed.
speed(0)

#Draw the outline box.
for i in range(2):
    forward(200)
    right(90)
    forward(140)
    right(90)

color("red")

def draw_bar():
    begin_fill()
    for i in range(2):
        forward(50)
        right(90)
        forward(140)
        right(90)
    end_fill()

draw_bar()
penup()
forward(150)
pendown()
draw_bar()
