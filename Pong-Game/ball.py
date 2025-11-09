from turtle import Turtle


class Ball(Turtle):
    """
    The Ball class represents the game ball, handling its movement and collisions.
    """

    def __init__(self):
        """
        Initializes the Ball object with initial settings.
        """
        super().__init__()  # Initialize the Turtle base class
        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("white")  # Set the color of the ball to white
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.x_move = 10  # Initial horizontal movement speed
        self.y_move = 10  # Initial vertical movement speed
        self.speed = 0.1  # Initial speed of the ball

    def move(self):
        """
        Move the ball by adjusting its x and y coordinates based on its current speed and direction.
        """
        new_x = self.xcor() + self.x_move  # Calculate the new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate the new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bounce_y(self):
        """
        Reverse the vertical direction of the ball upon collision with the top or bottom wall.
        """
        self.y_move *= -1  # Reverse the vertical movement direction

    def bounce_x(self):
        """
        Reverse the horizontal direction of the ball upon collision with a paddle and reduce its speed slightly.
        """
        self.x_move *= -1  # Reverse the horizontal movement direction
        self.speed *= 0.99  # Reduce the ball's speed slightly (slower over time)

    def reset(self):
        """
        Reset the ball's position to the center of the screen and reverse its horizontal direction.
        """
        self.goto(0, 0)  # Position the ball at the center of the screen
        self.bounce_x()  # Reverse the horizontal direction of the ball
