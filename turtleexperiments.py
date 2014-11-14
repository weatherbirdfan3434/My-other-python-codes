from turtle import *
import time
import random

def delay_and_clear():
    time.sleep(10)
    clear()

speed(0)
penup()
goto(-200, 200)
pendown()

for i in range(809):
    forward(400 - i)
    right(91)

penup()
goto(0, 0)
pendown()

delay_and_clear()

for i in range(360):
    circle(100)
    left(1)

right(1)

delay_and_clear()

for i in range(360):
    circle(i)
    left(1)

delay_and_clear()

penup()
goto(86, 86)
pendown()

left(45)
forward(172)
right(15)
for i in range(17):
    forward(20)
    right(15)
forward(172)
left(15)
for i in range(17):
    forward(20)
    left(15)
right(225)

penup()
goto(0, 0)
pendown()

delay_and_clear()

for i in range(40):
    forward(int(random.uniform(1, 100)))
    left(90)

penup()
goto(0, 0)
pendown()

delay_and_clear()

for i in range(40):
    forward(int(random.uniform(1, 100)))
    left(int(random.uniform(1, 100)))

penup()
goto(0, 0)
pendown()

delay_and_clear()

for i in range(int(random.uniform(1, 100))):
    forward(int(random.uniform(1, 100)))
    left(int(random.uniform(1, 100)))

penup()
goto(0, 0)
pendown()

delay_and_clear()

color("red")
begin_fill()
circle(120)
end_fill()
color("orange")
begin_fill()
circle(100)
end_fill()
color("yellow")
begin_fill()
circle(80)
end_fill()
color("green")
begin_fill()
circle(60)
end_fill()
color("blue")
begin_fill()
circle(40)
end_fill()
color("purple")
begin_fill()
circle(20)
end_fill()
