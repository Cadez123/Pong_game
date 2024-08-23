from turtle import Turtle

class Score(Turtle):
    def __init__(self, location):
        super().__init__()
        self.penup()
        self.goto(location)
        self.color('white')
        self.score = 0
        self.write(f'Score: {self.score}', align='left', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='left', font=('Arial', 20, 'normal'))

