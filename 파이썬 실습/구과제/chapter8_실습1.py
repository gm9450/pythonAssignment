# 실습1 : 마우스로 그림 그리기 기능 추가

# 추가된 기능
# 기능1 : 붓의 크기 조절 (팬의 크기를 입력받는 함수작동)
# 기능2 : 색깔 변경 (색 리스트에서 선택, 직접입력 함수작동)
# 기능3 : 간단한 그림 생성 (별, n각형)
# 기능4 : 리셋

import turtle

def draw(x, y):
    global m
    if (m == 1) :
        t.goto(x, y)
        s.listen()
    elif (m == 2) :
        t.up()
        t.goto(x, y)
        t.down()
        for i2 in range(5):
            t.fd(100)
            t.left(144)
        s.listen()
    elif (m == 3) :
        t.up()
        t.goto(x, y)
        t.down()
        n = int(turtle.textinput("모양 선택", "몇각형을 그릴까요?"))
        for i in range(n):
            t.fd(50)
            t.left(360/n)
        s.listen()

def function1():
    size = int(turtle.textinput("크기", "팬의 크기를 입력해주세"))
    t.pensize(size)
    s.listen()

def function2():
    num = -1
    colors = ["black", "red", "blue", "green", "yellow"]
    while not(num > 0 and num <= 6) :
        num = int(turtle.textinput("색",
                                 "1 : 검정색\n2 : 빨강색\n3 : 파랑색\n4 : 초록색\n5 : 노랑색\n6 : 직접 입력"))
        if (num > 0 and num <= 5):
            c = colors[num - 1]
            t.color(c)
            s.listen()
        elif (num == 6):
            c = turtle.textinput("직접 색 입력", "색을 입력해주세요.")
            t.color(c)
            s.listen()
        else :
            print("잘못된 입력입니다.")
            s.listen()
    s.listen()

def function3():
    global m
    m = int(turtle.textinput("모드", "1 : 기본\n2 : 별\n3 : n각형"))
    if (m > 3 or m <= 0):
        function(n)
    s.listen()

def function4():
    t.reset()
    t.pensize(6)

# default값
size = 6
color = "black"
m = 1

t = turtle.Turtle()
t.shape("turtle")
t.pensize(size)
s = turtle.Screen()

s.onscreenclick(draw)

s.onkey(t.penup, "Up")
s.onkey(t.pendown, "Down")
s.onkey(function1, "q")
s.onkey(function2, "w")
s.onkey(function3, "e")
s.onkey(function4, "r")
s.listen()
