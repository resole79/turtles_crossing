import display
from display import MyScreen
from turtle import Turtle

# Declare variable and CONSTANT
DISTANCE = 20
PENSIZE = 10
BORD_COLOR = "#F0C75E"
PEDESTRIAN_COLOR = "#FFFFFF"
RANGE_OF_BORD = display.MyScreen().y_coord // 33


# Class BordGame
class BordGame(Turtle):
    """ Class BordGame
    method:
    create_bord
    """
    def __init__(self):
        super().__init__()
        self.goto(0, MyScreen().y_coord)
        self.color(PEDESTRIAN_COLOR)
        self.pensize(PENSIZE)

    # Method to create bord
    def create_bord(self):
        """Method to create bord"""
        # Create pedestrian crossing
        for i in range(RANGE_OF_BORD):
            for m in range(3):
                self.pendown()
                self.setheading(0)
                self.forward(35)
                self.penup()
                self.setheading(270)
                self.forward(10)
                self.setheading(180)
                self.forward(35)
            self.penup()
            self.setheading(270)
            self.forward(50)

        self.goto(- MyScreen().x_coord + 10, MyScreen().y_coord - 50)
        # create end lines
        for i in range(4):
            self.color(BORD_COLOR)
            self.penup()
            self.forward(display.Y_SCREEN - DISTANCE-80)
            self.right(270)
            self.pendown()
            self.forward(display.X_SCREEN - DISTANCE)
            self.right(270)
