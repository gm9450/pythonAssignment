# 축구게임

# ---수정사항---
# 그래픽 이미지를 추가하였음

import random
import turtle

def graphic_choice1(n1, n2):
    t.goto(n1, n2)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(35)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    

def graphic_choice2(n1, n2):
    t.pendown()
    t.color("blue")
    t.goto(n1 ,n2)
    t.begin_fill()
    t.circle(25)
    t.end_fill()

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(-200, 200)
t.goto(200, 200)
t.goto(200, 0)
t.penup()
t.goto(-60, 0)

option=["중앙", "왼쪽 상단", "왼쪽 하단", "오른쪽 상단", "오른쪽 하단"]
computer_choice = random.choice(option)
while True :
    user_choice = turtle.textinput("", "어디를 수비하시겠어요?(중앙, 왼쪽 상단, 왼쪽 하단, 오른쪽 상단, 오른쪽 하단)")
    if (user_choice in option):
        if (computer_choice == user_choice) :
            t.write("패널티킥이 실패하였습니다.")
            break
        else:
            t.write("패널티킥이 성공하였습니다.")
            break

t.goto(0, 0)
if (computer_choice == option[0]):
    graphic_choice1(0, 80)
elif (computer_choice == option[1]):
    graphic_choice1(-130, 120)
elif (computer_choice == option[2]):
    graphic_choice1(-130, 20)
elif (computer_choice == option[3]):
    graphic_choice1(130, 120)
elif (computer_choice == option[4]):
    graphic_choice1(130, 20)

if (user_choice == option[0]):
    graphic_choice2(0, 80)
elif (user_choice == option[1]):
    graphic_choice2(-130, 120)
elif (user_choice == option[2]):
    graphic_choice2(-130, 20)
elif (user_choice == option[3]):
    graphic_choice2(130, 120)
elif (user_choice == option[4]):
    graphic_choice2(130, 20)

turtle.done()