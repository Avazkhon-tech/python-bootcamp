from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
rainbow_colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet']
all_turtles = []

y_position = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(y_position))
    y_position += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()






















