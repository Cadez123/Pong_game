from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

# screen setup
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)

# paddles setup
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

# paddle movements
screen.onkey(l_paddle.go_up,'Up')
screen.onkey(l_paddle.go_down,'Down')
screen.onkey(r_paddle.go_up,'w')
screen.onkey(r_paddle.go_down,'s')

ball = Ball()
l_score = Score((-250,250))
r_score = Score((100,250))


# game code
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 320) or ball.distance(r_paddle) < 20:
        ball.bounce_from_right_paddle()
        ball.move_speed *= 0.9

    if (ball.distance(l_paddle) < 40 and ball.xcor() < -320) or ball.distance(r_paddle) < 20:
        ball.bounce_from_left_paddle()
        ball.move_speed *= 0.9

    if ball.xcor() > 380:
        ball.reset_ball()
        l_score.add_point()
        time.sleep(1)

    if ball.xcor() < -380:
        ball.reset_ball()
        r_score.add_point()
        time.sleep(1)







screen.exitonclick()