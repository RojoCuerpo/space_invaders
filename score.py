from turtle import Turtle
import time

FONT_SCORE = "Times New Roman", 10, "bold"
GAME_OVER = "Times New Roman", 25, "bold"
SCORE_GAME_OVER = "Times New Roman", 15, "bold"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.p_1 = 0
        self.wave = 1
        self.hideturtle()
        self.penup()
        self.color("white")

    def write_wave(self):
        self.goto(x=0, y=305)
        self.write(arg=f"WAVE {self.wave}", align="center", font=FONT_SCORE)

    def write_score(self):
        self.goto(x=420, y=305)
        self.write(arg="SCORE", align="right", font=FONT_SCORE)
        self.goto(x=420, y=285)
        self.write(arg=round(self.p_1, 2), align="right", font=FONT_SCORE)

    def lives_write(self):
        self.goto(x=-420, y=305)
        self.write(arg="LIVES", align="left", font=FONT_SCORE)
        self.goto(x=-420, y=285)
        self.write(arg=self.lives, align="left", font=FONT_SCORE)

    def miss(self):
        self.p_1 -= 10
        self.clear()
        self.write_score()
        self.lives_write()
        self.write_wave()

    def invader_hit(self):
        self.p_1 += 125
        self.clear()
        self.write_score()
        self.lives_write()
        self.write_wave()

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.write_score()
        self.lives_write()
        self.write_wave()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=50)
        self.write(arg="GAME OVER", align="center", font=GAME_OVER)
        self.goto(x=0, y=15)
        self.write(arg=f"SCORE: {self.p_1}", align="center", font=SCORE_GAME_OVER)
        self.goto(x=0, y=-10)
        self.write(arg=f"WAVE: {self.wave}", align="center", font=SCORE_GAME_OVER)
        self.goto(x=0, y=-35)
        self.write(arg=f"Restart: 'space'", align="center", font=FONT_SCORE)
        self.goto(x=0, y=-55)
        self.write(arg=f"Close: 'q'", align="center", font=FONT_SCORE)
