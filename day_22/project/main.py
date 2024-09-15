from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import time

screen = Screen()
screen.setup(width=800, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Pong()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  pong.move()

  if pong.ycor() > 280 or pong.ycor() < -280:
    pong.bounce_y()

  if (pong.distance(r_paddle) < 50 and pong.xcor() > 320) or (pong.distance(l_paddle) < 50 and pong.xcor() < -320):
    pong.bounce_x()

  if pong.xcor() > 380 or pong.xcor() < -380:
    pong.reset_position()

screen.exitonclick()