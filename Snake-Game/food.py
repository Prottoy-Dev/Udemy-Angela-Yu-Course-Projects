from turtle import Turtle, Screen
import random

# Create a Turtle screen for the game
wn = Screen()


# image = r"C:\Users\Asus\Downloads\giphy_s (1).gif"
# wn.addshape(image)

class Food(Turtle):
    def __init__(self):
        super().__init__()

        # Set the appearance and attributes of the food item
        self.shape("circle")
        self.color("blue")
        # self.shape(image)
        self.penup()
        self.speed("fastest")

        # Place the initial food item on the screen
        self.refresh()

    def refresh(self):
        # Move the food item to a random position within the screen boundaries
        x = random.randint(-480, 480)
        y = random.randint(-480, 480)
        self.goto(x, y)
