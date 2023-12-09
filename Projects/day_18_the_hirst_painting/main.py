import turtle
#
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(len(color_list))

from turtle import Turtle, Screen
from random import choice
color_list = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204), (83, 70, 40), (11, 112, 106)]
tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.left(180)
tim.forward(400)
tim.left(90)
tim.forward(360)
tim.left(90)
tim.pendown()
tim.speed(0)
count = 0
for i in range(10):
    for j in range(10):
        tim.color(choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.pendown()















screen = Screen()
screen.exitonclick()



















