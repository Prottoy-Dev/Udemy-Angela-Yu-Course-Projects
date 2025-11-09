from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        # Load the high score from a file
        with open("data.txt") as file:
            self.highscore = int(file.read())

        # Initialize the current score to zero
        self.score = 0

        # Set up the turtle for displaying the score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 450)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        # Check if the current score is higher than the high score
        if self.score > self.highscore:
            self.highscore = self.score
            # Update the high score in the data file
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        # Reset the current score to zero and update the display
        self.score = 0
        self.update_score()

    def increase_score(self):
        # Increase the current score by 1 and update the display
        self.score += 1
        self.update_score()

    def update_score(self):
        # Clear the existing score display and write the updated score
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 24, "normal"))