def car_body(a, b) :    # a는 가로길이, b는 세로길이
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)

def car_wheel(r, a) :   # r의 반지름으로 바퀴를 만듬
    t.up()
    t.goto(r, -r)
    t.down()
    t.circle(r)
    t.up()
    t.goto(a-r, -r)
    t.down()
    t.circle(r)

x = int(input("가로길이를 입력해주세요 : "))
y = int(input("세로길이를 입력해주세요 : "))
r = int(input("바퀴의 반지름의 길이를 입력해주세요 : "))

import turtle
t = turtle.Turtle()
t.shape("turtle")

car_body(x, y)          # 차 몸체 그리기
car_wheel(r, x)         # 차 바퀴 그리기

turtle.done()
