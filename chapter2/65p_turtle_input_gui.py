import turtle
t = turtle.Turtle()
t.shape("turtle")

k = 1
while (k == 1):                 # k가 1일 동안 반복

    direction = int(input("오른쪽으로 회전하면 1, 왼쪽으로 회전하면 2를 입력해주세요 : "))
    if ( direction == 1) :
        r = int(input("오른쪽으로 어느 정도 각도로 회전할까요? : "))
        t.right(r)
    elif ( direction == 2) :
        r = int(input("왼쪽으로 어느 정도 각도로 회전할까요? : "))
        t.left(r)
    
    x = int(input("어느 정도 움직일까요? : "))
    t.fd(x)

    k = int(input("프로그램 계속은 1, 프로그램 종료는 아무키나 눌러주세요 : "))

turtle.done