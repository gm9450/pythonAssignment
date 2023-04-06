# 거북이 제어하기(141p)

# ---수정사항---
# 1,2,3,4 명령어로 작동
# 90도 회전, 이동하기를 할수 있음
# 종료(4번)시 문한루프를 탈출함

import turtle

t=turtle.Turtle()
t.shape("turtle")

t.width()

t.shapesize(3, 3)

while True:
    command = int(turtle.textinput("", "명령을 입력하시오.\n1 : 왼쪽으로 회전\n2 : 오른쪽으로 회전\n3 : 이동하기\n4 : 종료"))
    if (command == 1) :
        t.left(90)
    elif (command == 2) :
        t.right(90)
    elif (command == 3) :
        n = int(turtle.textinput("", "몇만큼 이동할까요?"))
        t.fd(n)
    elif (command == 4):
        break
    else :
        print("제대로 입력해주세요.")

print("종료되었습니다.")
turtle.done()