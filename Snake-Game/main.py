# Import necessary modules
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

# Create a Turtle screen for the game
tv = Screen()
tv.setup(width=1200, height=1000)
tv.bgcolor("black")
tv.title("Snake Game")
tv.listen()
tv.tracer(0)

# Create instances of the Snake, Food, and Score classes
snake = Snake()
food = Food()
score = Score()

# Set up keyboard controls for the snake's movement
tv.onkey(key="Up", fun=snake.up)
tv.onkey(key="Down", fun=snake.down)
tv.onkey(key="Left", fun=snake.left)
tv.onkey(key="Right", fun=snake.right)

# Initialize the game loop control variable
game_on = True

# Main game loop
while game_on:
    tv.update()
    time.sleep(0.05)
    snake.move()

    # Check if the snake has collided with the food
    if snake.head.distance(food) < 25:
        food.refresh()      # Generate a new food item
        snake.extend()      # Extend the snake
        score.increase_score()  # Increase the player's score

    # Check if the snake has collided with the screen boundaries
    if (
        snake.head.xcor() > 590
        or snake.head.ycor() > 500
        or snake.head.xcor() < -590
        or snake.head.ycor() < -500
    ):
        score.reset()   # Reset the player's score
        snake.reset()   # Reset the snake's position and length

    # Check for collisions with the snake's own body
    for segment in snake.body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            score.reset()   # Reset the player's score
            snake.reset()   # Reset the snake's position and length

# Close the game window when clicked
tv.exitonclick()
