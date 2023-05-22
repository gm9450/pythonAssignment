import turtle

def star_net(length):
    n = 2.7
    n1 = 6
    if (length >  300/n**n1):
        for i in range(5):
            t.fd(length)
            t.left(18)
            t.fd(length/2)
            t.left(18)
            star_net(length / n)
            t.right(18)
            t.backward(length/2)
            t.right(18)
            t.right(144)

t = turtle.Turtle()

t.speed(0)
turtle.bgcolor("black")
t.color("yellow")

t.penup()
t.goto(-100,0)
t.pendown()

# star(100)
star_net(200)

turtle.done()
