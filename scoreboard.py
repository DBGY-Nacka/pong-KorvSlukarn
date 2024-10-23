from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")
NAME_FONT = ("Arial", 24, "normal")
GAME_OVER_FONT = ("Arial", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, left_player, right_player):
        super().__init__()
        self.color("Red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.left_player = left_player
        self.right_player = right_player
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-200, 260)
        self.write(self.left_player, align=ALIGNMENT, font=NAME_FONT)
        self.goto(200, 260)
        self.write(self.right_player, align=ALIGNMENT, font=NAME_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def display_winner(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over! {winner} Wins!", align=ALIGNMENT, font=GAME_OVER_FONT)

    def reset_scores(self):
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()