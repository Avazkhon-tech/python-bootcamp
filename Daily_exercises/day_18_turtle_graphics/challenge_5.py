import random
import turtle
from turtle import Turtle, Screen
from random import randint

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = r, g, b
    return colour


tim = Turtle()
tim.shape("classic")
tim.speed(0)


def draw_spirograph(size):
    for _ in range(int(round(360 / size))):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
