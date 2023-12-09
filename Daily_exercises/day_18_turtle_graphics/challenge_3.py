from turtle import Turtle, Screen
tim = Turtle()

tim.penup()
tim.left(90)
tim.forward(100)
tim.right(90)
tim.pendown()

# for i in range(3):
#     tim.color('blue')
#     tim.forward(160)
#     tim.right(120)
#
# for i in range(4):
#     tim.color('gray')
#     tim.forward(160)
#     tim.right(90)
#
# for i in range(5):
#     tim.color('red')
#     tim.forward(160)
#     tim.right(72)
#
# for i in range(6):
#     tim.color('green')
#     tim.forward(160)
#     tim.right(60)
#
# for i in range(7):
#     tim.color('black')
#     tim.forward(160)
#     tim.right(51.43)
#
# for i in range(8):
#     tim.color('orange')
#     tim.forward(160)
#     tim.right(45)
#
# for i in range(9):
#     tim.color('yellow')
#     tim.forward(160)
#     tim.right(40)

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Cyan', 'Magenta', 'Turquoise', 'Lime', 'Indigo', 'Teal', 'Maroon', 'Olive', 'Navy', 'Gray', 'Silver', 'Gold']
from random import choice


def draw_shape(sides_p, angle_p):
    for _ in range(sides_p):
        tim.forward(160)
        tim.right(angle_p)


for i in range(3, 11):
    color = choice(colors)
    tim.color(color)
    sides = i
    angle = 360 / sides
    draw_shape(sides, angle)




































screen = Screen()
screen.exitonclick()
