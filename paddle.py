from turtle import Turtle
import globals_var
class Paddle(Turtle):
    

    def __init__(self, init_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("yellow")
        self.init_position = init_position
        self.goto(self.init_position[0], self.init_position[1])

    def up(self):
        self.goto(self.xcor(), self.ycor() + globals_var.MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - globals_var.MOVE_DISTANCE)
       