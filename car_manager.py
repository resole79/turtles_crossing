# import turtle
from turtle import Turtle
from random import choice
from display import MyScreen
from random import randint

# Declare variable and CONSTANT
# IMAGE = "./image/cow.gif"
# turtle.register_shape(IMAGE)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Class CarManager
class CarManager:
    """
    # Class CarManager
    # Instance
    list_of_car, speed_car
    Method:
    create_car, increase_speed, move_car
    """
    def __init__(self):
        self.list_of_car = []
        self.speed_car = MOVE_INCREMENT

    # Method to create car
    def create_car(self):
        """# Method to create car"""
        random_choice = randint(1, 6)
        if random_choice == 1:
            car = Turtle()
            car.penup()
            car.setposition(MyScreen().y_coord - 50, randint(- MyScreen().x_coord + 50, MyScreen().x_coord - 50))
            car.setheading(180)
            car.shape("square")
            # car.shape(IMAGE)
            car.color(choice(COLORS))
            car.shapesize(1, 2)
            self.list_of_car.append(car)

    # Method to increase speed of car
    def increase_speed(self):
        """# Method to increase speed of car"""
        self.speed_car += MOVE_INCREMENT

    # Method to move car
    def move_car(self):
        """# Method to move car"""
        for the_car in self.list_of_car:
            the_car.forward(self.speed_car)
            if the_car.xcor() < -MyScreen().x_coord:
                self.list_of_car.pop(self.list_of_car.index(the_car))
                MyScreen().this_window.update()
                the_car.goto(MyScreen().x_coord + 1000000, MyScreen().y_coord + 1000000, )
                
