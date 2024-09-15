from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_INCREMENT = 5
MOVE_INCREMENT = 2
START_SPEED = 5

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.speeds = {}
        self.level = 1
        self.create_car()

    def create_car(self):
        for _ in range(CAR_INCREMENT):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(random.randint(0, 300), random.randint(-250, 250))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)
            self.speeds[car] = random.randint(START_SPEED + MOVE_INCREMENT * (self.level - 1), START_SPEED + MOVE_INCREMENT * self.level)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speeds[car], car.ycor())
            if car.xcor() < -320:
                car.goto(320, car.ycor())

    def level_up(self):
        self.level += 1
        self.create_car()
