# n각형 그리기

# ---수정사항---
# 6개 원그리기를 수정하여 사용
# 원 대신 n1각형을 사용함
# n2번 회전 시킴

import turtle
t = turtle.Turtle()
t.width(2)
t.speed(0)

def t_figure(n, len):
    t.fd(len)
    t.left(360/n)

n1 = int(turtle.textinput("", "몇 각형을 그리겠습니까?"))
n2 = int(turtle.textinput("", "몇번 회전 시키겠습니까?"))
len = int(turtle.textinput("", "길이를 몇으로 하시겠습니까?"))
for i1 in range(n2):
    for i2 in range(n1):
        t_figure(n1, len)
    t.left(360/n2)

turtle.done()