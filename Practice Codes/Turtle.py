from turtle import color, back, left, forward, right, exitonclick
import turtle
import time

t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('black')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


t.penup()
t.goto(-80,300)
time.sleep(5)
t.pendown()
t.shapesize(1,2,1)

# Letter: 'I'
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=5)

t.begin_fill()

t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
# Height of the 'I'
t.fd(140)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(140)
t.left(90)
t.fd(60)
t.rt(90)
t.fd(25)

t.end_fill()

# End of 'I'
t.penup()
t.goto(-550,-20)
t.pendown()


# Draw 'Love'
# Letter: 'L'
t.pen(pencolor="white",fillcolor="red", pensize=2, speed=1)
t.begin_fill()

t.rt(90)
t.fd(25)
t.rt(90)
t.fd(165)
t.lt(90)
t.fd(115)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(140)
t.rt(90)
t.fd(190)
t.rt(90)

t.end_fill()
# End of 'L'

t.penup()
t.fd(140)

#Gap between 'L' and 'O'
t.fd(70)

# Letter: 'O'
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=4)
t.begin_fill()

t.rt(90)
t.fd(190)
t.lt(90)
t.pendown()
t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.rt(90)
t.pendown()
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# End of 'O'

#Gap between 'O' and 'V'
t.fd(100)
t.pendown()

# Letter: 'V'
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=2)
t.begin_fill()

t.lt(100)
t.fd(120)
t.rt(100)
t.fd(20)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(20)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(20)
t.rt(100)
t.fd(120)
t.rt(80)
t.fd(50)
t.lt(180)

t.end_fill()
# End of 'V'

t.penup()
# Gap between 'V' and 'E'
t.fd(100)
t.pendown()

# Letter: 'E'
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=2)
t.begin_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()
# End of 'E'


t.penup()
t.rt(180)
#Gap between 'E' and 'Y'
t.fd(200)
t.pendown()

# Letter: 'Y'
t.pen(pencolor="pink",fillcolor="red", pensize=1, speed=3)
t.begin_fill()

t.lt(90)
t.fd(50)
t.lt(30)
t.fd(80)
t.rt(120)
t.fd(20)
t.rt(60)
t.fd(60)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(20)
t.rt(120)
t.fd(80)
t.lt(30)
t.fd(50)
t.rt(90)
t.fd(20)
t.rt(180)

t.end_fill()
# End of 'Y'

t.penup()
t.fd(120)
t.pendown()

# Letter: 'O'
t.pen(pencolor="pink",fillcolor="red", pensize=1, speed=3)
t.begin_fill()

t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.pendown()
t.rt(90)
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# End of 'O'

# Gap between "O" and "U"
t.fd(100)
t.circle(60, extent=60)
t.pendown()

# Letter: 'U'
t.pen(pencolor="pink",fillcolor="red", pensize=1, speed=3)
t.begin_fill()

t.lt(30)
# Height of 'U'
t.fd(85)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(70)
t.circle(-20, extent=180)
t.fd(70)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(85)
t.circle(40, extent=180)

t.end_fill()
# End of 'U'

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(35)
t.lt(90)
t.fd(140)
t.lt(90)
t.pendown()



t.penup()
t.goto(-40,-330)

t.shapesize(1,4,1)
t.pen(pencolor="pink",fillcolor="red", pensize=2, speed=1)

t.begin_fill()

t.write("POOJA", move=True, align="center", font=("Lucida Sans", 70, "bold"))
t.pendown()

exitonclick()