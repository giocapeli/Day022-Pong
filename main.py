from turtle import Screen
from paddle import Paddle

#vars
game_on = True

#screen
s = Screen()
s.bgcolor("black")
s.screensize(600, 400)
s.title("Pong")
s.tracer(0) #turn off animation

#board

paddle_player = Paddle((290, 0))

paddle_pc = Paddle((-300, 0))

s.listen()
s.onkey(paddle_player.up, "Up")
s.onkey(paddle_player.down, "Down")

while game_on:
    s.update()

#exit
s.exitonclick()