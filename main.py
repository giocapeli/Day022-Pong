from turtle import Screen
from paddle import Paddle

#screen
s = Screen()
s.bgcolor("black")
s.screensize(600, 400)
s.title("Pong")

#board

paddle = Paddle()
paddle.goto(290, 0)

s.listen()
s.onkey(paddle.up, "Up")
s.onkey(paddle.down, "Down")

#exit
s.exitonclick()