# 정수의 부호에 따라 거북이를 움직이자(137p)

# ---수정사항---
# 입력한수를 그래픽에 표시함
# 원을 도차한곳에 원을 그림

import turtle
t = turtle.Turtle()
t.shape("turtle")

def red_circle(n):
    t.penup()
    t.goto(180, n)
    t.width(3)
    t.pendown()
    t.color("red")
    t.circle(20)

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수 입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0 입니다.")
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수 입니다.")

t.goto(0,0)
s = int(turtle.textinput("", "숫자를 입력하시오."))

t.write(str(s))

t.pendown()

if (s > 0):
    t.goto(100, 100)
    red_circle(90)
if (s == 0):
    t.goto(100, 0)
    red_circle(-10)
if (s < 0):
    t.goto(100, -100)
    red_circle(-110)

turtle.done()