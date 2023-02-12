from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("yellow")
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
                
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)