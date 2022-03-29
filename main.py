from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from tiles import Tiles
from scoreborad import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)


# opaddle = Turtle()

paddle = Paddle((0, -280))
screen.listen()

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
ball = Ball((0, -255))
tile = Tiles()
score = Scoreboard()
game_is_on = True
numberoftiles = 68

while len(tile.all_tiles) < numberoftiles :
    time.sleep(0.00001)
    screen.update()
    tile.createTile()

while game_is_on:
    # score.update_hscore()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #     ball.y_bounce()
    # if ball.distance(paddle) < 40 and ball.xcor() > 320  and ball.xcor() < -320:
    #     ball.x_bounce()
    if ball.xcor() > 380 :
        ball.x_bounce()
    if ball.xcor() < -380 :
        ball.x_bounce()

    if ball.distance(paddle) < 40 :
        ball.y_bounce()

    if ball.ycor() > 270:
        ball.y_bounce()

    if ball.ycor() < -270:
        score.game_over()
        score.update_hscore()
        game_is_on = False


    for one in tile.all_tiles:
        if ball.distance(one) < 30 :
            one.hideturtle()
            tile.all_tiles.remove(one)
            ball.y_bounce()
            score.win()





screen.exitonclick()