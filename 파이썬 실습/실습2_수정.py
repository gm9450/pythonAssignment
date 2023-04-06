# 삼각형의 길이가 같은 양변을 먼저 그린다. - 길이:100, 각:360/n
# 삼각형 두변을 중심으로 나머지 한변의 길이를 구한다. - 사인공식으로 구함
# 구한 길이로 n각형을 그린다. - 처음위치에서 for문으로 구하기
# 처음위치에서 각을 구함, 회전

# 수정사항
# 반지름의 길이 입력
# 외접원을 그림
# width값을 키움
# 반복횟수 입력을 추가함
# 색을 랜덤으로 추가함

# 삼각함수를 이용함
# 랜덤을 이용함
import random
import math
import turtle

# 함수로 만듬, n각형 만들기
def nangle(n, r):
    # 색을 랜덤으로 선택함
    i = random.randint(0, 4)
    t.color(colors[i])
    
    # 양변그리기 반복
    for i in range(n):
        t.fd(r)
        t.left(180 - 360/n)
        t.fd(r)
        t.right(180)

    # 180/n을 라디안으로 바꾼다
    x = math.radians(180/n)
    # 나머지 한변의 길이를 구한다
    y = 2*(r * math.sin(x))

    t.right(90-180/n)

    # n각형을 그림
    # y은 구해야 할 길이
    for i in range(n):
        t.fd(y)
        t.left(360/n)

t=turtle.Turtle()
t.width(3)

colors = ["red", "blue", "green", "yellow", "pink"]

num = int(turtle.textinput("반복할 횟수", "몇번 그릴 것인가요?"))
r = int(turtle.textinput("반지름", "반지름의 길이를 입력하시오"))

for i in range(num):
    n = int(turtle.textinput("n등분하기", "몇 등분 하시겠습니까"))
    nangle(n, r)
    t.left(90-180/n)

t.right(90-180/n)
i = random.randint(0, 4)
t.color(colors[i])

# 외접원 그리기
t.right(180/n)
t.circle(r)

turtle.done()