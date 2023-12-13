import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)
tim = Turtle()
tim.pensize(15)
tim.speed(50)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = r, g, b
    return colour


for i in range(100):
    tim.pencolor(random_color())
    num = randint(1, 3)
    if num == 1:
        tim.forward(30)
    elif num == 2:
        tim.left(90)
        tim.forward(30)
    elif num == 3:
        tim.right(90)
        tim.forward(30)




































screen = Screen()
screen.exitonclick()


