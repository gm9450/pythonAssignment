def turtle_fill_circle(c, r) :      #c의 색으로 채워진 r반지름의 원을 그리는 함수
    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def turtle_move(x, y) :             # 거북이를 x, y만큼 움직이는 함수
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.right(90)

import turtle
t = turtle.Turtle()
t.shape("turtle")

k = 1
while (k == 1):                      # k가 1일 동안 반복

    ficolor = input("색상을 입력해주세요(ex: blue, orange) : ")
    rd = int(input("반지름을 입력해주세요 : "))

    turtle_fill_circle(ficolor, rd)  # 원 그리기      

    x = int(input("x출으로 몇만큼 움직일까요? : "))
    y = int(input("y축으로 몇만큼 움직일까요? : "))
    turtle_move(x, y)                # 거북이 움직이기

    k = int(input("프로그램 계속은 1, 프로그램 종료는 아무키나 눌러주세요 : "))

turtle.done
