#가장 안쪽의 원은 반지름 10 - 처음 값을 10으로 설정
#원의 반지름은 5씩 증가 - 반복할때 마다 5씩 증가
#캔버 스배경은 검정색 - bgcolor()함수로 설정
#사용된 선 색깔의 순서는 r, p, b, g, y, o, p - for문으로 해결할것임

import turtle

colors = ["red","purple", "blue", "green", "yellow","orange", "pink"]
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(3)
radius = 10

for i in range(19*4):
    t.pencolor(colors[i % 7])
    t.circle(radius, 90)
    radius += 5

turtle.done()