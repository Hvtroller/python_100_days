from turtle import Turtle

class Pong(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.just_bounced = False

  def move(self):
    if self.just_bounced and ((self.x_move > 0 and self.xcor() > 0) or (self.x_move < 0 and self.xcor() < 0)):
      self.just_bounced = False

    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    if not self.just_bounced:
      self.just_bounced = True
      self.x_move *= -1

  def reset_position(self):
    self.goto(0, 0)
    self.bounce_x()
