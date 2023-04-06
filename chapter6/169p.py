# n개의 원 그리기(6개의 원 그리기)

# ---수정사항---
# n개의 원을 그릴수 있게 변경함

import turtle
t = turtle.Turtle()
t.width(2)
t.speed(0)

def tcircle(n):
    t.circle(100)
    t.left(360/n)

n = int(turtle.textinput("", "몇 번 반복하시겠습니까?"))
for i in range(n):
    tcircle(n)

turtle.done()