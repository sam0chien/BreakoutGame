from random import choice
from turtle import Turtle


class Brick(Turtle):
    colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown']

    def __init__(self, x, y):
        super().__init__()
        self.shapesize(1, 2.5)
        self.color(choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x, y)

    def get_hit(self):
        self.goto(1000, 1000)
