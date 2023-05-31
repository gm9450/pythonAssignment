import turtle
import random

# 충돌부분에 폭발모션을 넣음
# 높이를 출력함

def explode(x, y, k):
    explosion = turtle.Turtle()
    explosion.hideturtle()
    explosion.shape("circle")
    explosion.penup()
    explosion.goto(x, y)
    explosion.showturtle()

    explosion.shapesize(k/3)
    
    red = random.random()  # Generate a random value for the red channel (0-1)
    green = random.random()  # Generate a random value for the green channel (0-1)
    blue = random.random()  # Generate a random value for the blue channel (0-1)
    explosion.color(red, green, blue)

    explosion.stamp()

    explosion.hideturtle()
    screen.update()

width, height = 600, 300  # Game board size
gravity = 0.05  # Gravity
x, y = 0, height/2  # Ball position
vx, vy = 0.25, 1  # Ball velocity
coef_res = 0.90  # Coefficient of restitution

screen = turtle.Screen()
screen.setup(width + 100, height + 100)
screen.tracer(0)  # Manual screen update

ball = turtle.Turtle()
ball.color("orange", "black")
ball.shape("circle")
ball.up()
ball.goto(x, y)  # Move the ball to the starting position
ball.down()

while True:  # Animation loop
    x = x + vx  # Update the current position
    y = y + vy
    ball.goto(x, y)
    
    vy = vy - gravity  # Decrease the y-direction velocity due to gravity

    if (vy-gravity < 0 and vy > 0):
            ball.write(ball.ycor()+150) # 공의 y의 값 + 바닥의 y값

    if y < -height / 2:  # Collide with the ground
        explode(x, y, vy)
        vy = -vy * coef_res  # Decrease y-direction velocity and reverse direction
        ball.sety(-height / 2)  # Set the ball's y-coordinate to the ground level

    if x > width / 2 or x < -width / 2:  # Collide with the left/right walls
        screen.update()
        vx = -vx  # Reverse the x-direction velocity
    
    screen.update()  # Update the screen
