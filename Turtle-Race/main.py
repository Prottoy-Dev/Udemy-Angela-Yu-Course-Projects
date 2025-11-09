# Import the necessary modules from the Turtle graphics library
from turtle import Turtle, Screen
import random

# Create a screen object
tv = Screen()
tv.setup(width=500, height=400)

# Prompt the user to make a bet by guessing a color
user_input = tv.textinput(title="Make a bet", prompt="What color?")

# Define a list of colors that the turtles can have
colors = ["red", "green", "blue", "black", "yellow", "orange"]

# Create an empty list to store turtle objects
all_turtles = []

# Initialize a variable to control the game loop
game_on = True


# Function to position a turtle on the left side of the screen
def move_left(name, y_place):
    name.penup()
    name.goto(-245, y_place)


# Initial vertical position for the turtles
y = 190

# Create five turtle objects, each with a different color
for _ in range(5):
    x = Turtle("turtle")
    x.color(colors[_])
    move_left(x, y)  # Position the turtle on the left
    y -= 90  # Adjust the vertical position for the next turtle
    all_turtles.append(x)  # Add the turtle to the list

# Main game loop
while game_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))  # Move the turtle forward by a random distance
        if turtle.xcor() > 240:  # Check if the turtle has reached the right edge of the screen
            game_on = False  # End the game
            winner_color = turtle.pencolor()  # Get the color of the winning turtle
            if user_input.lower() == winner_color:  # Check if the user's guess matches the winning color
                print(f"You win. The winner is {winner_color.title()}")
            else:
                print(f"You lose. {winner_color.title()} is the winner")

# Wait for the user to click anywhere to exit the program
tv.exitonclick()
