from turtle import Turtle as T, Screen

class ScoreBoard:

    def __init__(self):
        self.score = 0
        self.score_board = T()
        self.score_board.color("white")
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.goto(0, 270)
        self.score_board.write(f"Score: {self.score} ", False, "center", font=('Arial', 15, 'normal'))

    def update_score_board(self):
        self.score += 1
        self.score_board.clear()
        self.score_board.write(f"Score: {self.score} ", False, "center", font=('Arial', 15, 'normal'))

    def game_over(self):
        game_over = T()
        game_over.penup()
        game_over.color("white")
        game_over.hideturtle()
        game_over.write("GAME OVER", False, "Center", font=('Arial', 25, 'normal'))