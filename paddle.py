from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,location):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(location)


    def go_up(self):
        x = self.xcor()
        y = self.ycor() + 60
        self.goto(x,y)

    def go_down(self):
        x = self.xcor()
        y = self.ycor() - 60
        self.goto(x,y)

