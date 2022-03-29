from turtle import Turtle
import random


NEW_X = -430
NEW_Y = 255
NUMBER_TILES = 68

class Tiles(Turtle):
    def __init__(self):
        self.all_tiles = []
        self.x = NEW_X
        self.y = NEW_Y
        self.all_tiles = []
        self.createTile()

    def createTile(self):

        new_tile = Turtle("square")
        new_tile.shapesize(stretch_wid=1, stretch_len=2)
        new_tile.penup()

        if self.x < 380:
            new_x = self.x + 50
            new_y = self.y
            new_tile.goto((new_x, new_y))
            self.x = new_tile.xcor()
            self.y = new_tile.ycor()
        else:
            self.x = -380
            self.y = self.y - 40
            new_tile.goto((self.x, self.y))

        new_tile.color("white")
        self.all_tiles.append(new_tile)


