import turtle

def circle(r):
    if (r >= 100/3/3/3/3 and  r < 100):
        circle1(r)
        circle1(r)
        circle1(r)
        circle1(r)
        circle1(r)
    elif (r == 100):
        t.circle(r, 360/5)
        circle(r/3)
        t.circle(r, 360/5)
        circle(r/3)
        t.circle(r, 360/5)
        circle(r/3)
        t.circle(r, 360/5)
        circle(r/3)
        t.circle(r, 360/5)
        circle(r/3)

def circle1(r):
    t.right(180)
    t.circle(r, 360/5)
    circle(r/3)
    t.left(180)

t = turtle.Turtle()
t.shape("turtle")

t.speed(0)
t.penup()
t.goto(0, -100)
t.down()
circle(100)

turtle.done()