from turtle import Turtle
import random


class Invaders(Turtle):
    def __init__(self):
        super().__init__()
        self.all_invaders = []
        self.brick = None
        self.x_move = 5

        self.bomb_steps = -10
        self.all_bombs = []

    def rows(self):
        y = 260
        x = -425
        for i in range(5):
            alien = Turtle("square")
            alien.color("black")
            alien.fillcolor("white")
            alien.setheading(180)
            alien.penup()
            alien.turtlesize(stretch_wid=1, stretch_len=1)
            alien.goto(x, y)
            self.all_invaders.append(alien)
            x += 40

        y = 240
        x = -405
        for i in range(4):
            alien = Turtle("square")
            alien.color("black")
            alien.fillcolor("white")
            alien.setheading(180)
            alien.penup()
            alien.turtlesize(stretch_wid=1, stretch_len=1)
            alien.goto(x, y)
            self.all_invaders.append(alien)
            x += 40

        y = 220
        x = -385
        for i in range(3):
            alien = Turtle("square")
            alien.color("black")
            alien.fillcolor("white")
            alien.setheading(180)
            alien.penup()
            alien.turtlesize(stretch_wid=1, stretch_len=1)
            alien.goto(x, y)
            self.all_invaders.append(alien)
            x += 40

        y = 200
        x = -365
        for i in range(2):
            alien = Turtle("square")
            alien.color("black")
            alien.fillcolor("white")
            alien.setheading(180)
            alien.penup()
            alien.turtlesize(stretch_wid=1, stretch_len=1)
            alien.goto(x, y)
            self.all_invaders.append(alien)
            x += 40

        y = 180
        x = -345
        alien = Turtle("square")
        alien.color("black")
        alien.fillcolor("white")
        alien.setheading(180)
        alien.penup()
        alien.turtlesize(stretch_wid=1, stretch_len=1)
        alien.goto(x, y)
        self.all_invaders.append(alien)

    def move_invaders(self):
        for i in self.all_invaders:
            new_x = i.xcor() + self.x_move
            i.goto(new_x, i.ycor())

    def bounce_right(self):
        self.x_move = -5

    def bounce_left(self):
        self.x_move = 5

    def bomb(self):
        chance = random.randint(1, 5)
        if chance == 1:
            try:
                shooter = random.choice(self.all_invaders)
                bomb = Turtle()
                bomb.setheading(-90)
                bomb.shape("square")
                bomb.hideturtle()
                bomb.penup()
                bomb.color("red")
                bomb.fillcolor("red")
                bomb.shapesize(stretch_wid=.1, stretch_len=.5)
                bomb.goto(shooter.xcor(), shooter.ycor())
                bomb.showturtle()
                self.all_bombs.append(bomb)
            except IndexError:
                pass




