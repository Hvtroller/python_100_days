# turle colors
https://trinket.io/docs/colors

# Draw a dashed line

```python
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=100)

for _ in range(10):
  timmy.forward(10)
  timmy.penup()
  timmy.forward(10)
  timmy.pendown()

screen.exitonclick()
```

# Draw random shapes

```python
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=100)

for i in range(3, 10):
  for _ in range(i):
    timmy.forward(100)
    timmy.right(360/i)

screen.exitonclick()
```

# Draw a random direction

```python
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

timmy.speed("fastest")
for i in range(300):
  timmy.color(random_color())
  timmy.forward(random.randint(10, 30))
  if random.randint(0, 1):
    timmy.right(random.randint(0, 360))
  else:
    timmy.left(random.randint(0, 360))

screen.exitonclick()
```

# Draw Spirograph

```python
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

timmy.speed("fastest")
for i in range(360//5):
  timmy.color(random_color())
  timmy.circle(100)
  timmy.setheading(timmy.heading() + 5)

screen.exitonclick()
```