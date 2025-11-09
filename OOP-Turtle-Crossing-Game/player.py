from turtle import Turtle


class Player(Turtle):
    """
    Represents the player's turtle in the game.

    Methods:
        up(): Move the turtle upwards.
        down(): Move the turtle downwards.
        reset(): Reset the turtle's position to the starting point.
    """

    def __init__(self):
        """Create a new player turtle."""
        super().__init__()  # Initialize the turtle
        self.shape("turtle")  # Set the shape of the turtle
        self.setheading(90)  # Set initial direction (facing upwards)
        self.penup()  # Lift the pen to avoid drawing
        self.goto(0, -280)  # Position the turtle at the starting point
        self.speed("fastest")  # Set the movement speed

    def up(self):
        """Move the turtle upwards."""
        self.forward(20)  # Move the turtle forward by 20 units

    def down(self):
        """Move the turtle downwards."""
        self.forward(-20)  # Move the turtle backward by 20 units

    def reset(self):
        """Reset the turtle's position to the starting point."""
        self.goto(0, -280)  # Position the turtle at the starting point
