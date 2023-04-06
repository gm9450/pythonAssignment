import turtle
t = turtle.Turtle()
t.shape("turtle")
num = int(input("몇번 실행할까요? : "))

for k in range(num):                         # num번 반복
    n = int(input("몇각형을 그릴까요? : "))     # 각도 입력
    degree = 360/n
    for i in range(n) :
        t.forward(10)
        t.left(degree)

    print("turtle을 움직여주세요")              # 거북이 움직이기
    move_x = int(input("x : "))
    move_y = int(input("y : "))

    # 움직일때 선이 그어지지 않게 함
    t.up()
    t.goto(move_y, move_y)
    t.down()

turtle.done
