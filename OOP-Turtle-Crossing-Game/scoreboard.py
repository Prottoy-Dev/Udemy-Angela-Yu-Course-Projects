from turtle import Turtle

class Scoreboard(Turtle):
    """
    Represents the game's scoreboard.

    Attributes:
        score (int): The current game level.
        fast (float): The speed multiplier for game elements.
    """

    def __init__(self):
        """Create a new scoreboard."""
        super().__init__()
        self.score = 0  # Initialize the score to 0
        self.fast = 0.5  # Initialize the speed multiplier
        self.hideturtle()  # Hide the default turtle cursor
        self.update_score()  # Display the initial score

    def update_score(self):
        """Update and display the current score on the screen."""
        self.clear()  # Clear the previous score display
        self.penup()  # Lift the pen to avoid drawing
        self.goto(-320, 250)  # Position the scoreboard
        self.write(f"Level:{self.score}", align="center", font=("Courier", 24, "normal"))

    def lvl_up(self):
        """Increase the game level and update the score."""
        self.score += 1  # Increment the game level
        self.fast *= 0.9  # Adjust the speed multiplier
        self.update_score()  # Display the updated score

    def game_over(self):
        """Display 'Game Over' on the screen."""
        self.goto(0, 0)  # Position the text in the center of the screen
        self.write("Game Over", align="center", font=("Courier", 80, "normal"))
