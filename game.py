from turtle import *
import turtle
from ship import Ship
from score import Score
from invaders import Invaders
import time

paused = True
game_on = True


def main():
    screen = Screen()
    screen.clear()
    screen.bgcolor("black")
    screen.title("Space_Invaders")
    screen.setup(width=900, height=680)
    screen.listen()
    screen.tracer(0)

    ship = Ship((0, -320))
    screen.update()
    time.sleep(.5)

    score = Score()
    score.write_wave()
    time.sleep(.5)
    score.lives_write()
    time.sleep(.5)
    score.write_score()
    screen.update()
    time.sleep(.5)

    invaders = Invaders()
    invaders.rows()

    screen.onkeypress(ship.shoot, "space")

    def ship_position(event):
        global paused
        if not paused:
            new_x = event.x - 450
            ship.goto(x=new_x, y=-320)
        else:
            pass
    ws = turtle.getcanvas()
    ws.bind('<Motion>', ship_position)

    def quit_game():
        global game_on
        game_on = False

    def pause_game():
        global paused
        if paused:
            paused = False
        else:
            paused = True

    pause_game()
    screen.onkey(pause_game, "BackSpace")

    global game_on
    game_on = True
    while game_on:
        while not paused:
            screen.update()
            invaders.move_invaders()
            invaders.bomb()
            time.sleep(.01)

            if score.lives == 0:
                pause_game()
                game_on = False

            for i in invaders.all_bombs:
                try:
                    i.forward(10)
                    if i.distance(ship) < 20:
                        i.hideturtle()
                        score.decrease_lives()
                        invaders.all_bombs.remove(i)
                except ValueError:
                    pass

            for i in invaders.all_invaders:
                try:
                    if i.xcor() > 420:
                        invaders.bounce_right()
                    if i.xcor() < -420:
                        invaders.bounce_left()
                except ValueError:
                    pass

            for x in ship.all_shots:
                try:
                    x.forward(10)
                    for y in invaders.all_invaders:
                        if x.distance(y) < 10:
                            score.invader_hit()
                            y.hideturtle()
                            x.hideturtle()
                            ship.all_shots.remove(x)
                            invaders.all_invaders.remove(y)
                            if len(invaders.all_invaders) == 0:
                                score.lives += 1
                                score.p_1 += score.p_1
                                score.wave += 1
                                invaders.rows()
                                screen.update()
                                time.sleep(3)
                    if x.ycor() > 400:
                        ship.all_shots.remove(x)
                        x.hideturtle()
                        score.miss()
                except ValueError:
                    pass
        else:
            screen.update()
            screen.onkey(quit_game, "q")

    score.game_over()
    screen.onkey(main, "space")
    screen.onkey(quit, "q")
    screen.exitonclick()


main()
