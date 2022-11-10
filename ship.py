from turtle import Turtle


class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.fillcolor("white")
        self.tilt(90)
        self.shape("triangle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(position)
        self.showturtle()

        self.laser = Turtle()
        self.laser.shape("square")
        self.laser.hideturtle()
        self.laser.penup()
        self.laser.color("white")
        self.laser.fillcolor("white")
        self.laser.shapesize(stretch_wid=.5, stretch_len=.1)
        self.all_shots = []

    def shoot(self):
        laser = Turtle()
        laser.setheading(90)
        laser.shape("square")
        laser.hideturtle()
        laser.penup()
        laser.color("green")
        laser.fillcolor("green")
        laser.shapesize(stretch_wid=.1, stretch_len=.5)
        laser.goto(self.xcor(), self.ycor())
        self.all_shots.append(laser)
        laser.showturtle()


