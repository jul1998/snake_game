from turtle import Turtle as T, Screen
import random
screen = Screen()
position = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
directions = [0, 180, 90, 270]
colors = ["red", "blue", "yellow", "green"]

class CreateSnake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for segment in range(3):
            new_segment = T("square")
            new_segment.penup()
            new_segment.color(colors[segment])
            new_segment.goto(position[segment])
            self.segments.append(new_segment)

    def extend(self):
        choice_color = random.choice(colors)
        new_segment = T("square")
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color(choice_color)
        new_segment.penup()
        self.segments.append(new_segment)

    def right(self):
        if self.snake_head.heading() != directions[1]:
            self.snake_head.setheading(directions[0])

    def left(self):
        if self.snake_head.heading() != directions[0]:
            self.snake_head.setheading(directions[1])

    def up(self):
        if self.snake_head.heading() != directions[3]:
            self.snake_head.setheading(directions[2])

    def down(self):
        if self.snake_head.heading() != directions[2]:
            self.snake_head.setheading(directions[3])

    def move_all_snakes(self):
        for seg_number in range(len(self.segments) -1, 0, -1):
            new_x_cor = self.segments[seg_number-1].xcor()
            new_y_cor = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(new_x_cor, new_y_cor)
        self.snake_head.forward(distance)

    def difficulty(self):
        global distance
        choose_difficulty = screen.numinput("Difficulty", "Choose difficulty: 1,2 or 3", 1, minval=1, maxval=4)
        # choose_difficulty = int(input("Choose difficulty: 1,2 or 3 -> "))
        if choose_difficulty == 1:
            distance = 20
        elif choose_difficulty == 2:
            distance = 25
        elif choose_difficulty == 3:
            distance = 30