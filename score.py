from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.goto(0, 250)
        self.color("yellow")
        self.write(f'{self.score_p1}    -    SCORE    -     {self.score_p2}', move=False, align='center', font=('Arial', 25, 'normal'))
        self.hideturtle()

    def update_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.write(f'{self.score_p1}    -    SCORE    -     {self.score_p2}', move=False, align='center', font=('Arial', 25, 'normal'))
    
    def update_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.write(f'{self.score_p1}    -    SCORE    -     {self.score_p2}', move=False, align='center', font=('Arial', 25, 'normal'))
