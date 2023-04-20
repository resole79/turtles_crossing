from display import MyScreen
from turtle import Turtle

# Declare variable and CONSTANT
DISTANCE_FOR_SCORE = 40
FONT = ("Courier", 15, "bold")
ALIGN = "center"
GAME_OVER_IMAGE = "./image/turtle_cross.png"


# Class Scoreboard
class Scoreboard(Turtle):
    """
    Class Scoreboard
    Instance:
    level
    Method:
    game_over, increase_level, refresh_score
    """
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("#FF0000")
        self.penup()
        self.hideturtle()
        self.goto(-220, MyScreen().y_coord - DISTANCE_FOR_SCORE)
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        MyScreen().this_window.bgpic(GAME_OVER_IMAGE)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1

    def refresh_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
