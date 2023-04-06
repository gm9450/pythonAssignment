# 가위바위보 게임(그래픽 버전)

# 1,2로 시작과 종료를 할수 있음
# 가위바위보 게임으로 변경
# 가위(0) > 보(2) > 바위(1) > 가위(0)
# 가위바위보를 숫자로 변환하는 함수
# 숫자를 가위바위보 글자로 변환하는 함수
# 컴퓨터와 사람의 승패를 판단하는 함수
# 승패에 따라 문장을 출력해주는 함수

# ---수정사항---
# 그래픽 이미지를 추가함
# 승패를 터틀그래픽에서 출력

import turtle
import random

# 글자를 숫자로 변경 ex)가위 -> 0
def RPS(n):
    if (n == '가위'):
        return 0
    elif (n == '바위'):
        return 1
    elif (n == '보'):
        return 2
    else:
        return 3

# 숫자를 글자로 변경 0 -> 가위
def URPS(n):
    if (n == 0):
        t1.shape(image1)
        t1.stamp()
        return '가위'
    elif (n == 1):
        t1.shape(image2)
        t1.stamp()
        return '바위'
    elif (n == 2):
        t1.shape(image1)
        t1.stamp()
        return '보'
    else:
        return "잘못됨"

# a1는 컴퓨터, a2는 사람
# 승패를 판단함
def RPS_j(a1, a2):
    if (a1 == 0):
        if (a2 == 0):
            return '비김'
        elif (a2 == 1):
            return '승리'
        else:
            return '패배'
    elif (a1 == 1):
        if (a2 == 0):
            return '패배'
        elif (a2 == 1):
            return '비김'
        else:
            return '승리'
    elif (a1 == 2):
        if (a2 == 0):
            return '승리'
        elif (a2 == 1):
            return '패배'
        else:
            return '비김'

# 결과 출력
def j_p(n):
    if (n == '승리'):
        print("당신이 이겼습니다.")
    elif(n == '패배'):
        print("당신이 졌습니다.")
    elif (n == '비김'):
        print("서로 비겼습니다.")
       
# 처음 실행되는 부분
screen = turtle.Screen()
image1 = "S.gif"
image2 = "R.gif"
image3 = "P.gif"
screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)

t1 = turtle.Turtle()
t1.penup()
t1.goto(-100, 150)
t1.write("컴퓨터")
t1.goto(100, 150)
t1.write("당신")
message = "처음 시작"
while True:
    command = int(turtle.textinput(message, "명령어를 입력해주세요.\n1 : 시작\n2 : 종료"))
    turtle.clear()
    if (command == 1) :
        a1 = random.randrange(3)
        while True:
            a2 = turtle.textinput("", "무엇을 낼까요?\n(가위, 바위, 보)")
            a2 = RPS(a2)
            if (a2 < 3):
                break
            print("잘못 된 값이에요.")
        print("----------------")
        t1.goto(-100, 0)
        print("컴퓨터 :", URPS(a1))
        t1.goto(100,0)
        print("사람 :", URPS(a2))
        j_p(RPS_j(a1, a2))
        print("----------------\n")
        message = RPS_j(a1, a2)
    elif (command == 2) :
        break
    else :
        print("제대로 입력해주세요.")