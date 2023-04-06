# 조건이 거짓일 때 연속하여 다른 조건을 검사

# ---수정사항---
# 정수의 부호에 따라 거북이를 움직이자(137p)를 수정함
# if가 3번 사용됬는데 이를 if, elif 형식으로 변경함

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
elif (s == 0):
    t.goto(100, 0)
    red_circle(-10)
elif (s < 0):
    t.goto(100, -100)
    red_circle(-110)

turtle.done()