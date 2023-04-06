# 삼각형의 길이가 같은 양변을 먼저 그린다. - 길이:100, 각:360/n
# 삼각형 두변을 중심으로 나머지 한변의 길이를 구한다. - 코사인 공식
# 구한 길이로 n각형을 그린다. - 처음위치에서 for문으로 구하기
# 처음위치에서 각을 구함, 회전

# l은 구해야 할 길이
import math
import turtle

t=turtle.Turtle()

n = int(turtle.textinput("등분하", "몇 등분 하시겠습니까"))

# 양변그리기 반복
for i in range(n):
    t.fd(100)
    t.left(180 - 360/n)
    t.fd(100)
    t.right(180)

# 180/n을 라디안으로 바꾼다
x = math.radians(180/n)
# 나머지 한변의 길이를 구한다
y = 2*(100 * math.sin(x))

t.right(90-180/n)

# n각형을 그림
# y은 구해야 할 길이

for i in range(n):
    t.fd(y)
    t.left(360/n)

turtle.done()