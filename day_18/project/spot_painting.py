import colorgram
from turtle import Turtle, Screen
import random

def extract_colors(image_path, num_colors):
  colors = colorgram.extract(image_path, num_colors)
  rgb_colors = []
  for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
  return rgb_colors

turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=1200, startx=0, starty=0)
turtle.speed("fastest")

turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()

image_colors = extract_colors("day_18/project/sample.jpg", 30)

for _ in range(10):
  for _ in range(10):
    turtle.dot(20, random.choice(image_colors))
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
  turtle.penup()
  turtle.backward(500)
  turtle.right(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.pendown()

turtle.hideturtle()
screen.exitonclick()
