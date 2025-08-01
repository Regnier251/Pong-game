from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
import time

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"i")
screen.onkey(r_paddle.go_down,"k")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision paddlles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()
        
screen.exitonclick()