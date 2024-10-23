import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

        # Player names
        self.left_player = self.screen.textinput("Player Name", "Enter left player name:")
        self.right_player = self.screen.textinput("Player Name", "Enter right player name:")

        self.ball = Ball()
        self.right_paddle = Paddle((350, 0))
        self.left_paddle = Paddle((-350, 0))
        self.scoreboard = Scoreboard(self.left_player, self.right_player)

        self.screen.listen()
        self.screen.onkeypress(self.right_paddle.move_up, "Up")
        self.screen.onkeypress(self.right_paddle.move_down, "Down")
        self.screen.onkeypress(self.left_paddle.move_up, "w")
        self.screen.onkeypress(self.left_paddle.move_down, "s")
        self.screen.onkeypress(self.right_paddle_win, "o")#lite fusk ifall jag förlorar
        self.screen.onkeypress(self.restart_game, "r")

        self.game_speed = 0.1
        self.initial_ball_speed = 0.1 

    def run(self):
        game_is_on = True
        while game_is_on:
            start_time = time.time()

            self.screen.update()
            self.ball.move()

            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            if (self.ball.distance(self.right_paddle) < 50 and self.ball.xcor() > 320) or \
               (self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() < -320):
                self.ball.bounce_x()
                self.increase_speed()

            if self.ball.xcor() > 380:
                self.scoreboard.l_point()
                self.reset_positions()
            elif self.ball.xcor() < -380:
                self.scoreboard.r_point()
                self.reset_positions()

            if self.scoreboard.l_score == 10 or self.scoreboard.r_score == 10:
                game_is_on = False
                self.display_game_over()

            elapsed_time = time.time() - start_time
            time.sleep(self.game_speed)

        self.screen.exitonclick()

    def increase_speed(self):
        self.game_speed *= 0.9

    def reset_positions(self):
        self.ball.reset_position()
        self.right_paddle.goto(350, 0)
        self.left_paddle.goto(-350, 0)
        self.reset_game()

    def reset_game(self):
        self.game_speed = self.initial_ball_speed

    def display_game_over(self):
        self.scoreboard.display_winner(self.left_player if self.scoreboard.l_score == 10 else self.right_player)
        self.screen.update()
        time.sleep(3)  

    def right_paddle_win(self):
        self.scoreboard.r_score = 10
        self.display_game_over()

    def restart_game(self):
        self.reset_game()
        self.scoreboard.reset_scores()
        self.run()

if __name__ == "__main__":
    game = Game()
    game.run()