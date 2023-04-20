from turtle import Turtle

# Declare variable and CONSTANT
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280
PLAYER_COLOR = "#FF0000"
PLAYER_SHAPE = "turtle"
TOP = 90


# CLass Player
class Player(Turtle):
    """# CLass Player
    Method:
    player_up, refresh_player
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.refresh_player()
        self.setheading(TOP)

    def player_up(self):
        self.setheading(TOP)
        self.forward(MOVE_DISTANCE)

    def refresh_player(self):
        self.goto(STARTING_POSITION)
