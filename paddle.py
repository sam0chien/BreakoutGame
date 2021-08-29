from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("skyblue")
        self.shapesize(1, 5)
        self.penup()
        self.goto(0, -260)

    def go_left(self):
        if self.xcor() >= -340:  # bound control
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() <= 340:  # bound control
            new_x = self.xcor() + 40
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, -260)
