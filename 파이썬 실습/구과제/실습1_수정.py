#가장 안쪽의 원은 반지름 10 - 처음 값을 10으로 설정
#원의 반지름은 5씩 증가 - 반복할때 마다 5씩 증가
#캔버 스배경은 검정색 - bgcolor()함수로 설정
#사용된 선 색깔의 순서는 r, p, b, g, y, o, p - for문으로 해결할것임

#수정사항
#반복횟수 입력을 추가
#원의 각도 입력을 추가함
#추가되는 반지름값 입력을 추가

import turtle

colors = ["red","purple", "blue", "green", "yellow","orange", "pink"]
t = turtle.Turtle()
turtle.bgcolor("black")

n1 = int(turtle.textinput("반복", "반복할 횟수를 입력해주세요"))
angle = int(turtle.textinput("각", "각도를 적어주세요"))
plus = int(turtle.textinput("추가되는 반지름", "길이를 입력해주세요"))

#int로 저장하지 않으면 실행되지 않음
n2 = int(360 / angle)

t.speed(0)
t.width(3)
radius = 10

#끝나는 위치를 고정하기 위해서 n2라는 값을 사용, 90에 딱나눠지는 수만 가능함
for i in range(n1*n2):
    t.pencolor(colors[i % 7])
    t.circle(radius, angle)
    radius += plus

turtle.done()