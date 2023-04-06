def turtle_cir_mov(r, x):       # r반지름의 원을 그리고 x만큼 움직임
    t.circle(r)
    t.fd(x)

import turtle
t = turtle.Turtle()
t.shape("turtle")

k = 1
while (k == 1):                 # k가 1일 동안 반복

    radius = int(input("반지름을 입력해주세요 : "))
    x = int(input("x축으로 이동할 거리를 입력해주세요. : "))

    turtle_cir_mov(radius, x)   # 원 그리고 움직임

    k = int(input("프로그램 계속은 1, 프로그램 종료는 아무키나 눌러주세요 : "))

turtle.done