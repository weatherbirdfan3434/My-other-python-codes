from turtle import *

#Assign variables.
c = 67
b = 0

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

#Draw the blue rectangle.
color("blue")
begin_fill()
for i in range(2):
    forward(100)
    right(90)
    forward(70)
    right(90)
end_fill()

#Prepare the turtle to draw the stripes
penup()
forward(100)
pendown()
color("red")

#Draw the upper stripes.
for i in range(4):
    begin_fill()
    forward(100)
    right(90)
    forward(10)
    right(90)
    forward(100)
    end_fill()
    left(90)
    penup()
    forward(10)
    pendown()
    left(90)

#Prepare the turtle to draw the lower stripes.
backward(100)

def draw_red_long_stripe():
    begin_fill()
    forward(200)
    right(90)
    forward(10)
    right(90)
    forward(200)
    end_fill()

#Draw the lower stripes.
for i in range(2):
    draw_red_long_stripe()
    left(90)
    penup()
    forward(10)
    pendown()
    left(90)
draw_red_long_stripe()

#Prepare the turtle to draw the stars.
left(108)
penup()
goto(-90, c)
pendown()
color("white")

def draw_star():
    begin_fill()
    for i in range(5):
        forward(3)
        left(72)
        forward(3)
        right(144)
    end_fill()

#Draw the stars.
while True:
    draw_star()
    penup()
    goto(-74, c)
    pendown()
    draw_star()
    penup()
    goto(-58, c)
    pendown()
    draw_star()
    penup()
    goto(-42, c)
    pendown()
    draw_star()
    penup()
    goto(-26, c)
    pendown()
    draw_star()
    penup()
    goto(-10, c)
    pendown()
    draw_star()
    b = b + 1
    if b == 9:
        break
    else:
        c = c - 7
    penup()
    goto(-82, c)
    pendown()
    draw_star()
    penup()
    goto(-66, c)
    pendown()
    draw_star()
    penup()
    goto(-50, c)
    pendown()
    draw_star()
    penup()
    goto(-34, c)
    pendown()
    draw_star()
    penup()
    goto(-18, c)
    pendown()
    draw_star()
    b = b + 1
    if b == 9:
        break
    else:
        c = c - 7
    penup()
    goto(-90, c)
    pendown()

#Move the turtle out of the way.
penup()
goto(-400, 400)

