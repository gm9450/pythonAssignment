import turtle
import math
import random

# 터틀의 방향을 더 세부적으로 조절할 수 있음
# 비행기를 맞추는 기능을 추가함
# 비행기를 맞추거나 바닥에 닿으면 폭발함

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def turnup():
    player.setheading(90)

def turndown():
    player.setheading(270)

def explode(x, y):
    explosion = turtle.Turtle()
    explosion.hideturtle()
    explosion.shape("circle")
    explosion.color("red")
    explosion.penup()
    explosion.goto(x, y)
    explosion.showturtle()

    for _ in range(5):
        size = random.randint(5, 20)
        explosion.shapesize(size / 10)
        explosion.stamp()
        explosion.color(random.random(), random.random(), random.random())

    explosion.hideturtle()


def fire():
    x = -300  # 초기 좌표
    y = 0  # 초기 좌표
    player.color(random.random(), random.random(), random.random())
    player.goto(x, y)  # (x, y) 위치로 간다
    angle = player.heading()  # 초기각도
    vx = velocity * math.cos(angle * math.pi / 180.0)  # 도 -> 라디안
    vy = velocity * math.sin(angle * math.pi / 180.0)  # 도 -> 라디안

    while player.ycor() >= 0:  # y좌표가 음수가 될 때까지
        vx = vx  # x 방향 속도는 변경이 없다.
        vy = vy - 10  # y 방향 속도는 중력 가속도 만큼 감소
        x = x + vx  # 1초가 지났으므로 속도를 위치에 더한다.
        y = y + vy  # 1초가 지났으므로 속도를 위치에 더한다.
        player.goto(x, y)  # 새로운 위치로 이동시킨다.
        player.stamp()  # 거북이를 찍는다.
        if is_collision(player, enemy):
            game_over()
            break
    
    explode(x, y)  # 호출되면 폭발 효과를 생성
    player.goto(-300, 0)  # (x, y) 위치로 간다

def move_enemy():
    enemy.forward(5)  # 적 비행기를 아래로 이동시킴

    # 적 비행기가 화면 아래로 나가면 다시 상단으로 이동시킴
    if enemy.ycor() < -300:
        enemy.goto(-300, 100)

    if enemy.xcor() > 200:
        enemy.goto(-300, 100)

    turtle.ontimer(move_enemy, 100)  # 일정한 시간 간격으로 move_enemy 함수 호출

def is_collision(t1, t2):
    distance = t1.distance(t2)  # 두 객체 간의 거리 계산
    return distance < 20  # 거리가 20보다 작으면 충돌로 판단

def game_over():
    enemy.goto(-300, 100)
    player.clear()

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
screen.bgcolor("black")  # 화면 배경을 검정색으로 한다.
screen.setup(800, 600)  # 화면의 크기를 800×600으로 한다.
player.color("yellow")  # 색상은 파랑색으로 하자.
player.goto(-300, 0)
velocity = 70  # 초기속도 70픽셀/sec
player.left(45)
enemy = turtle.Turtle()
enemy.shape("triangle")
enemy.color("red")
enemy.penup()
enemy.goto(-300, 100)  # 적 비행기 초기 위치 설정

move_enemy() # 적 비행기 움직이기 시작

screen.onkeypress(turnleft, "Left")  # 콜백함수 등록
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.onkeypress(fire, "space")
screen.listen()
turtle.mainloop()
