#!/usr/bin/env python3

from turtle import Turtle, Screen
import random

def random_color():
  r = random.random()
  g = random.random()
  b = random.random()
  return (r, g, b)

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=100)

# timmy.shape("turtle")
# timmy.color("red")
timmy.speed("fastest")
for i in range(360//5):
  timmy.color(random_color())
  timmy.circle(100)
  timmy.setheading(timmy.heading() + 5)

screen.exitonclick()
