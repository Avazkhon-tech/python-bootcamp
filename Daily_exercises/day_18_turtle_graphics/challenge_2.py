# draw a dash line
from turtle import Turtle, Screen
tim = Turtle()

for _ in range(2):
    for i in range(10):
        tim.forward(10)
        tim.color('white')
        tim.forward(10)
        tim.color('black')

    tim.left(90)
    for i in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.left(90)


screen = Screen()
screen.exitonclick()


