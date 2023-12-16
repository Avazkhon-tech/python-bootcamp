from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt", 'r') as file:
    HIGHSCORE = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGHSCORE
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("data.txt", 'w') as file:
            file.write(f'{self.highscore}')
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
