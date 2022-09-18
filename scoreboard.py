from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.points = 0
        self.mess = f"Score = {self.points}"
        self.write(self.mess, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.points += 1
        self.mess = f"Score = {self.points}"
        self.write(self.mess, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
