# 랜덤
import random

# 거북이
import turtle
t = turtle.Turtle()
t.shape("turtle")

# 채운 원 그리기
def ficircle(i, r):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# 터틀 움직이기
def tgoto (x, y):
    t.up()
    t.goto(x, y)
    t.down()

# 색상 리스트
color_list = []
n = int(turtle.textinput("색상입력", "색상을 몇개 입력할까요?"))
for i in range(n):
    color = turtle.textinput("색" ,"색상을 입력해주세요.\n(red, blue, green, yellow)")
    color_list.append(color)

n1 = int(turtle.textinput("원의 갯수", "원을 몇개 그릴까요?"))
for k in range(n1):
    # 거북이 이동
    x = int(turtle.textinput("x축", "x축으로 어디로 이동할까요?"))
    y = int(turtle.textinput("y축", "y축으로 어디로 이동할까요?"))
    tgoto(x, y)

    # 원그리기, i는 랜덤 색, r은 반지름
    i = random.randint(0, n-1)
    r = int(turtle.textinput("반지름", "반지름의 길이를 어떻게 할까요?"))    
    ficircle(i, r)

turtle.done()