from turtle import *
import time

def delay_and_clear():
    time.sleep(10)
    clear()

speed(0)

for i in range(150):
    penup()
    forward(i + 5)
    right(2*i + 10)
    pendown()
    stamp()

delay_and_clear()

penup()
goto(250, 100)
pendown()

for i in range(200):
    forward(200 - i)
    right(45)

delay_and_clear()

penup()
goto(250, 100)
pendown()

for i in range(200):
    forward(200/(i + 1))
    right(45)

delay_and_clear()

penup()
goto(200, 200)
pendown()

for i in range(400):
    forward(10 + 200/(i + 1))
    right(10)

delay_and_clear()

penup()
goto(0, 0)
pendown()

left(90)

forward(130)
circle(30)
forward(130)

delay_and_clear()

penup()
goto(0, 0)
pendown()

for i in range(4):
    forward(100)
    left(225)
    circle(30)
    right(135)

delay_and_clear()

penup()
goto(0, -200)
pendown()

for i in range(36):
    forward(30)
    left(185)
    circle(10)
    right(175)

#These are tries that prodduced interesting results.

#for i in range(36):
#    forward(50)
#    left(185)
#    circle(10)
#    right(15)
