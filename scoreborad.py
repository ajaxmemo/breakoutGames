from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.hscore = 0
        self.update_score()
        self.show_hscore()

    def update_score(self):
        self.clear()
        self.goto(250, 270)
        self.write(f" Your Score : {self.score}", align="center", font=("Courier", 15, "normal"))


    def win(self):
        self.score += 1
        self.update_score()
        self.show_hscore()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 15, "normal"))
        self.update_hscore()

    def show_hscore(self):
        data = open("data.txt")
        hscore = data.read()
        self.hscore= hscore
        self.goto(-250, 270)
        self.write(f" High Score : {self.hscore}", align="center", font=("Courier", 15, "normal"))

    def update_hscore(self):

        if self.score > int(self.hscore):
            # print(hscore)
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")





