from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, turtle_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(turtle_position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        # new_y = self.ycor() - 20
        # self.goto(self.xcor(), new_y)
