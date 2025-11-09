# Import necessary libraries
import turtle  # For graphics
from turtle import Turtle  # For car creation
import random  # For randomness

# Set color mode to RGB (0-255)
turtle.colormode(255)


class Car(Turtle):
    """
    Represents cars in the game.
    """

    def __init__(self):
        """Create a new Car."""
        super().__init__()  # Initialize the car
        self.all_cars = []  # Store car objects
        self.hideturtle()  # Hide the default cursor

    def make_cars(self):
        """Create and add a new car."""
        timmy = Turtle()  # Create a new car
        timmy.penup()  # Don't draw while moving
        timmy.shape("square")  # Car shape
        # Randomly set car color using RGB
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.shapesize(stretch_wid=1, stretch_len=2)  # Adjust car size
        # Randomly position the car within boundaries
        timmy.goto(x=random.randint(250, 550), y=random.randint(-250, 250))
        self.all_cars.append(timmy)  # Add the new car

    def move(self):
        """Move all cars to the left."""
        for cars in self.all_cars:
            cars.forward(-20)  # Move cars to the left
