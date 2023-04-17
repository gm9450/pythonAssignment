from turtle import *
import random
import turtle

# 클릭한 부분의 반대 방향으로 도망가기

colorList = ['red', 'blue', 'orange', 'purple', 'brown', 'pink', 'green']


class MyTurtle(Turtle):
    def run(self, x, y):
        self.fillcolor(random.choice(colorList))
        r = self.towards(x, y)
        self.setheading(r + 180)
        total_move = random.randrange(10, 100)
        a = 0
        b = 0
        for i in range(total_move):
            if (-400 < a < 400 and -400 < b < 400):
                self.fd(1)
                (a, b) = self.position()
            else:
                break
        if (-400 >= a or a >= 400 or -400 >= b or b >= 400):
            self.right(180)
            self.fd(10)


t = MyTurtle()
t.shape("turtle")
t.width(3)

s = turtle.Screen()
s.onscreenclick(t.run)
s.listen()
