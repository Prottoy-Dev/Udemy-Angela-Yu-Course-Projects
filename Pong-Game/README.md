# Pong-Game
## Here's an overview of the key components and how they come together:

1. Ball Class (Ball):
Represents the game ball with attributes for shape, color, and movement.
Manages ball movement, collision detection with walls and paddles, and speed adjustment.
Allows for resetting the ball's position and direction when scoring.

2. Puddle Class (Puddle):
Represents a player's paddle with shape, color, and size attributes.
Handles paddle movement within vertical game bounds using the "up" and "down" methods.

3. Scoreboard Class (Scoreboard):
Manages and displays the scores of both players.
Provides methods for updating and displaying the scores when a point is scored.

4. Main Body:
Initializes the game screen, sets up event listeners for paddle control, and defines the game loop.
Controls the flow of the game, including ball movement, collision detection, and score updates.
Allows the user to exit the game by clicking on the screen.
## Gameplay Overview:

The game starts with the ball in the center and the score set to 0-0.
Players control their respective paddles with arrow keys (right player) and "w" and "s" keys (left player).
The ball moves horizontally and vertically, bouncing off walls and paddles.
Scoring occurs when the ball passes beyond a paddle.
The game continues until the user decides to exit.
