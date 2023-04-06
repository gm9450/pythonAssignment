# 도형 그리기

# ---수정사항---
# 삼각형부터 유각형까지 그릴 수 있음
# 이름으로 입력함

import turtle
t = turtle.Turtle()
t.shape("turtle")

n = 0
s = turtle.textinput("", "도형을 입력하시오 : \n(삼각형부터 육각형까지)")
if (s == "삼각형"):
    n = 3
elif (s == "사각형"):
    n = 4
elif (s == "오각형"):
    n = 5
elif (s == "육각형"):
    n = 6
t.begin_fill()
for i in range(n):
    t.fd(100)
    t.left(360/n)
t.end_fill()

turtle.done()