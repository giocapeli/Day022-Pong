from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
import globals_var
#vars
game_on = True

#screen
s = Screen()
s.screensize(globals_var.BOARD_X, globals_var.BOARD_Y, "black")
s.title("Pong")
s.tracer(0) #turn off animation

#board

paddle_player = Paddle((globals_var.BOARD_X/ 2 -10, 0))
paddle_pc = Paddle((-(globals_var.BOARD_X)/ 2, 0))
ball = Ball()

s.listen()
s.onkey(paddle_player.up, "Up")
s.onkey(paddle_player.down, "Down")
s.onkey(paddle_pc.up, "w")
s.onkey(paddle_pc.down, "s")

while game_on:
    time.sleep(globals_var.SPEED)
    s.update()
    ball.move()
    if ball.ycor() >= globals_var.BOARD_Y/ 2 or ball.ycor() <= - globals_var.BOARD_Y/ 2:
        ball.change_direction_y()
    if (ball.xcor() >= (globals_var.BOARD_X)/ 2 - 20 and ball.distance(paddle_player) <= 50) or (ball.xcor() <= -(globals_var.BOARD_X)/ 2 + 20 and ball.distance(paddle_pc) <= 50):
        ball.change_direction_x()
        

#exit
s.exitonclick()