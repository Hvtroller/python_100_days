from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.read_high_score()
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} | High score: {self.highest_score}", align=ALIGMENT, font=FONT)

  def reset(self):
    if self.score > self.highest_score:
      self.save_high_score()
    self.score = 0
    self.update_scoreboard()

  def save_high_score(self):
    self.highest_score = self.score
    with open("day_20/project/high_score.txt", mode="w") as file:
      file.write(str(self.highest_score))
      file.close()

  def read_high_score(self):
    with open("day_20/project/high_score.txt") as file:
      self.highest_score = int(file.read())
      self.update_scoreboard()
      file.close()