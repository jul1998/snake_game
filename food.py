from turtle import Turtle as T, Screen
import random

class Food:

    def __init__(self):
        self.food = T()
        self.food.hideturtle()
        self.food = T("square")
        self.food.color("yellow")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.food.goto(x=random_x, y=random_y)