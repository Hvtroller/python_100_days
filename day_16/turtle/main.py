from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

screen = Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

# Calculate center position
center_x = (screen_width - 300) // 2
center_y = (screen_height - 300) // 2

# Set the screen size and position
screen.setup(width=500, height=500, startx=center_x, starty=center_y)

# Exit on click
screen.exitonclick()
