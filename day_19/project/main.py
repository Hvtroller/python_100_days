from turtle import Turtle, Screen
import random
from tkinter import messagebox

screen = Screen()
screen.setup(width=800, height=500, startx=0, starty=0)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
turtles = []

def draw_line(x_position):
  line = Turtle()
  line.penup()
  line.goto(x_position, 250)
  line.pendown()
  line.goto(x_position, -250)

draw_line(-250)
draw_line(250)

for i in range(len(colors)):
  turtle = Turtle(shape="turtle")
  turtle.color(colors[i])
  turtle.penup()
  y_position = -125 + i * 50
  turtle.goto(x=-250, y=y_position)
  turtles.append(turtle)


def move_forward(target):
  target.penup()
  target.forward(random.randint(0, 10))
  target.pendown()

do_break = False
while not do_break:
  for turtle in turtles:
    move_forward(turtle)
    if turtle.xcor() >= 250:
      messagebox.showinfo("Race Result", f"{turtle.pencolor()} wins!")
      do_break = True
      break

screen.exitonclick()