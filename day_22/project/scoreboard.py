from turtle import Turtle

FONT = ("Courier", 40, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.goto(0, 200)
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"{self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)