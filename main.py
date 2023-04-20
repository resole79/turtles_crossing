import time
from display import MyScreen
from player import Player
from car_manager import CarManager
from bord import BordGame
from scoreboard import Scoreboard

# Declare variable
game_is_on = True

# call class and initialize "MyScreen", "BordGame", "Scoreboard", "Player", "CarManager"
screen = MyScreen()
my_bord = BordGame()
my_scoreboard = Scoreboard()
michelangelo_the_turtle = Player()
lightning_the_car = CarManager()

screen.listen_player(michelangelo_the_turtle)
my_bord.create_bord()

# Cycle "while" condition to exit game_on equal to false
while game_is_on:
    time.sleep(0.1)
    # "for" to read alla car in list
    for car in lightning_the_car.list_of_car:
        # "if" to check distance between car and turtle
        if michelangelo_the_turtle.distance(car) < 25:
            my_scoreboard.game_over()
            game_is_on = False

    # "if" to check turtle cross street
    if michelangelo_the_turtle.ycor() <= MyScreen().y_coord:
        lightning_the_car.create_car()
        lightning_the_car.move_car()
    else:
        my_scoreboard.increase_level()
        my_scoreboard.refresh_score()
        lightning_the_car.increase_speed()
        michelangelo_the_turtle.refresh_player()

    screen.this_window.update()

screen.this_window.mainloop()
