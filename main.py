from turtle import Turtle, Screen
import random

colorMode = Screen()
colorMode.colormode(255)

x = Turtle()
x.hideturtle()


def settings():
    x.penup()
    x.setpos(-300, -300)
    x.shape('triangle')
    x.speed('fast')


settings()

paint = 0

while paint < 10:
    for i in range(10):
        color_list = [(190, 249, 246), (180, 249, 250), (208, 160, 101), (150, 75, 37), (231, 213, 97), (120, 251, 247),
                      (210, 247, 250), (132, 34, 21), (191, 156, 15), (87, 33, 21)]
        r_colors = random.choice(color_list)
        x.color(r_colors)
        x.dot(20)
        x.forward(50)
    x.left(90)
    x.forward(40)
    x.setx(-300)
    paint += 1
    x.right(90)

screen = Screen()
screen.exitonclick()






































