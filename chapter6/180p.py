# 별그리기 그리기

# ---수정사항---
# 6개 원그리기를 수정하여 사용
# 원 대신 n각형을 사용함

import turtle
t = turtle.Turtle()
t.width(1)
t.speed(0)

def t_figure(n, len):
    t.fd(len)
    t.left(720/n)

n = int(turtle.textinput("", "몇 번 회전 시킬까요?"))
for i1 in range(n):
    for i2 in range(5):
        t_figure(5, 300)
    t.left(360/n)

turtle.done()