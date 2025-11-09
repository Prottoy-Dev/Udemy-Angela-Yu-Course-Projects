from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time

# Create a game screen
game_screen = Screen()
game_screen.tracer(0)  # Turn off automatic screen updates
game_screen.title("Turtle Crossing")
game_screen.setup(height=600, width=800)
game_screen.listen()

# Create game objects
scoreboard = Scoreboard()
player = Player()
car = Car()

# Set up player controls
game_screen.onkey(key="Up", fun=player.up)
game_screen.onkey(key="Down", fun=player.down)

# Initialize game state
game_on = True

# Main game loop
while game_on:
    time.sleep(scoreboard.fast)  # Pause to control game speed
    game_screen.update()  # Update the game screen
    car.make_cars()  # Create new cars
    car.move()  # Move cars
    for cars in car.all_cars:
        # Check for collision with player
        if cars.distance(player) < 20:
            game_on = False  # End the game on collision
            scoreboard.game_over()  # Display "Game Over" message
    if player.ycor() > 280:
        player.reset()  # Reset player's position
        scoreboard.lvl_up()  # Increase game level on successful crossing

game_screen.exitonclick()  # Close the game window on click
