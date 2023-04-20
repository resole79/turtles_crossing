from turtle import Screen

# Declare variable and CONSTANT
X_SCREEN = 600
Y_SCREEN = 600
SCREEN_COLOR = "#000000"
SCREEN_TITLE = "Turtle Crossing"

up = "Up"

x_coordinate = X_SCREEN // 2
y_coordinate = Y_SCREEN // 2


# Class MyScreen
class MyScreen:
    """Class MyScreen
    # Instance
    list_of_window, this_window, x_coord, y_coord
    Method:
    create_window, listen_player
    """
    def __init__(self):
        self.list_of_window = []
        self.create_window()
        self.this_window = self.list_of_window[0]
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate

    # Method to create window
    def create_window(self):
        """Method to create window"""
        window = Screen()
        window.colormode(255)
        window.setup(X_SCREEN, Y_SCREEN)
        window.bgcolor(SCREEN_COLOR)
        window.title(SCREEN_TITLE)
        window.tracer(0)
        self.list_of_window.append(window)

    # Method to listen onkey press
    def listen_player(self, player):
        """Method to listen onkey press
        player -> object
        """
        for screen in self.list_of_window:
            screen.listen()
            screen.onkey(player.player_up, up)
