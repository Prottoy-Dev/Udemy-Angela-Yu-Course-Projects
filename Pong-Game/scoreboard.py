from turtle import Turtle


class Scoreboard(Turtle):
    """
    The Scoreboard class manages the game score and displays it on the screen.
    """

    def __init__(self):
        """
        Initializes the Scoreboard object with initial scores and settings.
        """
        super().__init__()  # Initialize the Turtle base class
        self.color("white")  # Set the color of the text to white
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.hideturtle()  # Hide the turtle cursor
        self.l_score = 0  # Initialize the left player's score to 0
        self.r_score = 0  # Initialize the right player's score to 0
        self.update_score()  # Call the update_score method to display the initial scores

    def update_score(self):
        """
        Clears the current score display and updates it with the latest scores.
        """
        self.clear()  # Clear any previous text on the screen
        self.goto(-100, 200)  # Move the turtle to the left player's score position
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Display the left player's score
        self.goto(100, 200)  # Move the turtle to the right player's score position
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Display the right player's score

    def l_point(self):
        """
        Increments the left player's score and updates the score display.
        """
        self.l_score += 1  # Increment the left player's score by 1
        self.update_score()  # Call update_score to display the updated score

    def r_point(self):
        """
        Increments the right player's score and updates the score display.
        """
        self.r_score += 1  # Increment the right player's score by 1
        self.update_score()  # Call update_score to display the updated score
