from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.backward(10)


def move_anticlockwise():
    tim.circle(-100, 10)


def move_clockwise():
    tim.circle(100, 10)


def clear_everything():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=turn_left)
screen.onkey(key='a', fun=move_anticlockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_everything)

screen.exitonclick()
