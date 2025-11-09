# Import necessary modules
from turtle import Screen
from puddle import Puddle  # a Puddle class for paddles
from ball import Ball  # a Ball class for the game ball
from scoreboard import Scoreboard  # a Scoreboard class
import time

# Initialize the game screen
tv = Screen()
tv.bgcolor("black")
tv.setup(width=800, height=600)
tv.title("Pong")
tv.tracer(0)  # Turn off automatic screen updates
score = Scoreboard()  # Create a scoreboard instance

# Create the right and left paddles and the ball objects
r_puddle = Puddle(350, 0)  # Right paddle starting position
l_puddle = Puddle(-350, 0)  # Left paddle starting position
ball = Ball()  # Create a ball instance

# Listen for key events to control paddles
tv.listen()
tv.onkeypress(key="Up", fun=r_puddle.up)  # Right paddle move up
tv.onkeypress(key="Down", fun=r_puddle.down)  # Right paddle move down
tv.onkeypress(key="w", fun=l_puddle.up)  # Left paddle move up
tv.onkeypress(key="s", fun=l_puddle.down)  # Left paddle move down

game_on = True  # Game loop control flag
while game_on:
    time.sleep(ball.speed)  # Control the speed of the game
    tv.update()  # Update the screen
    ball.move()  # Move the ball

    # Check for wall collisions and bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for paddle collisions and bounce the ball
    if (
        ball.xcor() > 320 and ball.distance(r_puddle) < 50
    ) or (ball.xcor() < -320 and ball.distance(l_puddle) < 50):
        ball.bounce_x()

    # Check for scoring conditions and reset the ball and update the score
    if ball.xcor() > 380:
        ball.reset()  # Reset the ball to the center
        score.l_point()  # Increment the left player's score
    if ball.xcor() < -380:
        ball.reset()  # Reset the ball to the center
        score.r_point()  # Increment the right player's score