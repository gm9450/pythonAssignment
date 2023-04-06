# 랜덤 사각형 그리기

# ---수정사항---
# 사각형대신 3~9각형까지로 설정함

import turtle
import random
t = turtle
t.shape("turtle")
t.speed(0)

def t_figure(n, len):
    t.fd(len)
    t.left(360/n)

def r_form():
    n1 = random.randint(3, 9)
    len = random.randint(1, 50)
    for i2 in range(n1):
        t_figure(n1, len)

for i in range(30):
    t.fillcolor(random.random(), random.random(), random.random())

    t.up()
    t.goto(random.randint(-100, 100), random.randint(-100, 100))
    t.down()

    length = random.randint(10, 100)
    height = random.randint(10, 100)
    t.begin_fill()
    r_form()
    t.end_fill()

turtle.done()
