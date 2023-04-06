def turtle_Square(n) :                          # n 길이의 삼각형을 그리는 함수
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)

print("사각형을 그리겠습니다.\n")
n = input("사각형의 한변의 길이는 몇으로 할까요? : ") # 삼각형의 길이를 입력받음
n = int(n)

import turtle
t = turtle.Turtle()
t.shape("turtle")

turtle_Square(n)                                 # 원 그리기

turtle.done()