import random
from turtle import *

# 크기가 작은 gif파일을 얻지 못해서 기본 모양으로 진행
# 변경사항
# 색, 모양, 크기 리스트를 추가함
# reinit메소드를 추가하였음
# reinit메소드를 반복 구문에 넣어서 속도, 색, 크기를 다시 정하게 함


class Car:
    def __init__(self, speed, color, fname, size):
        self.turtle = Turtle()
        self.turtle.width(size)
        self.turtle.color(color)
        self.turtle.shape(fname)
        self.turtle.speed(speed)
        self.turtle.shapesize(size)

    def drive(self, distance):
        self.turtle.forward(distance)

    def turnleft(self, degree):
        self.turtle.left(degree)

    def reinit(self):
        self.turtle.speed(random.randint(1, 10))
        self.turtle.color(random.choice(color_list))
        self.turtle.shapesize(random.choice(size_list))
        self.turtle.width(random.choice(size_list))


car_list = []			# 빈 리스트를 생성한다.
shape_list = ['classic', 'arrow', 'turtle', 'circle', 'square', 'triangle']
size_list = [0.7, 1, 1.5, 2, 2.5]
color_list = ['red', 'blue', 'orange', 'purple', 'brown', 'pink', 'green']
for _ in range(10):
    car_list.append(Car(random.randint(1, 10), "black",
                    random.choice(shape_list), 1))

for _ in range(10):  # 10번 반복
    for car in car_list:
        car.drive(random.randint(50, 100))
        car.turnleft(random.choice([0, 90, 180, 270]))
        car.reinit()
