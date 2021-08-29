from turtle import Turtle


class Over(Turtle):

    def __init__(self, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.write(text, move=True, align='center', font=("Arial", 50, "bold"))
