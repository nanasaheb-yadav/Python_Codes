import turtle
import time

t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('black')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


t.penup()
t.goto(-60,-330)

t.shapesize(1,4,1)
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=1)

t.begin_fill()

t.write("POOJA", move=True, align="center", font=("Cooper Black", 70, "bold"))
t.pendown()
time.sleep(2)