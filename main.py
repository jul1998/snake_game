from turtle import Turtle as T, Screen
from create_snake import CreateSnake
from food import Food
from score_board import ScoreBoard
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.delay(0)


#This creates 3 initial segments for snake
snake = CreateSnake()

#Create food
food = Food()

#Create score board
score_board = ScoreBoard()

#Select difficulty
snake.difficulty()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

screen.listen()



on = True
while on:
    screen.update()
    time.sleep(0.1)
    if snake.snake_head.distance(food.food) < 19:
        food.refresh()
        snake.extend()
        score_board.update_score_board()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score_board.game_over()
        break

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 15:
            on = False
            score_board.game_over()

    snake.move_all_snakes()


screen.exitonclick()
