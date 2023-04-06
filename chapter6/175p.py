# 거북이를 랜덤하게 움직이게 하자

# ---수정사항---
# 30번 -> 10번 반복으로 수정
# 반복여부를 물어봄

import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

while True:
    for i in range(10):
        length = random.randint(1, 100)
        t.fd(length)
        angle = random.choice([90, 180, 270])
        t.right(angle)
    n = int(turtle.textinput("", "1 : 종료\n(계속하려면 다른숫자 입력)"))
    if (n == 1):
        break
    else :
        continue
turtle.done()