from turtle import Turtle


class Puddle(Turtle):
    """
    The Puddle class represents a player's paddle, managing its position and movement.
    """

    def __init__(self, x, y):
        """
        Initializes the Puddle object with initial settings.

        Args:
            x (int): The initial x-coordinate of the paddle.
            y (int): The initial y-coordinate of the paddle.
        """
        super().__init__()  # Initialize the Turtle base class
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.turtlesize(stretch_wid=5, stretch_len=1)  # Adjust the size of the paddle
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.goto(x, y)  # Position the paddle at the specified coordinates

    def up(self):
        """
        Move the paddle upwards within the game's vertical bounds.
        """
        if self.ycor() <= 250:  # Check if the paddle is within the upper bound
            new_y = self.ycor() + 20  # Calculate the new y-coordinate
            self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def down(self):
        """
        Move the paddle downwards within the game's vertical bounds.
        """
        if -250 <= self.ycor():  # Check if the paddle is within the lower bound
            new_y = self.ycor() - 20  # Calculate the new y-coordinate
            self.goto(self.xcor(), new_y)  # Move the paddle to the new position

