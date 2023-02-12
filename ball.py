from turtle import Turtle
import globals_var
from random import randint

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("yellow")
        self.move_y = globals_var.MOVE_DISTANCE
        self.move_x = globals_var.MOVE_DISTANCE
        self.speed = globals_var.SPEED
        
    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def change_direction_y(self):
        # self.random_bounce()
        self.move_y *= -1
        
    def change_direction_x(self):
        # self.random_bounce()
        self.move_x *= -1
        self.speed *= 0.9
    
    def reset(self):
        self.change_direction_x()
        self.speed = globals_var.SPEED
        self.goto(0,0)
                
    # def random_bounce(self):
    #     self.move_x = randint(3, globals_var.MOVE_DISTANCE) * self.direction_x
    #     self.move_y = randint(3, globals_var.MOVE_DISTANCE) * self.direction_y