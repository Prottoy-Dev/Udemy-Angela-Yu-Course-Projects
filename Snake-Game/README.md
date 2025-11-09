# Snake-Game
The Snake Game is a classic arcade-style game implemented in Python using the Turtle graphics library. The player controls a snake that moves around the screen, eats food items to grow, and attempts to achieve the highest score while avoiding collisions with the screen boundaries and its own body.In the provided code, there are both built-in modules and custom classes created for a game. Let's provide a proper description to clarify which modules are built-in and which classes are custom-made for the game.

## Built-in Modules:
turtle (from turtle import Turtle, Screen):
The turtle module is a built-in Python module used for creating graphics and drawing. It provides the basic functionality for creating windows, drawing shapes, and controlling the turtle's movements.

random (import random):
The random module is a built-in Python module used for generating random numbers. In the code, it's used to randomize the position of the food item on the game screen.

## Custom Classes:
Snake (class Snake:):
The Snake class is a custom-made class representing the snake character in the game. It is responsible for managing the snake's body, movement, growth, and direction.

Food (class Food(Turtle):):
The Food class is another custom-made class representing the food item in the game. It controls the appearance and position of the food item on the screen and handles refreshing its location when the snake eats it.

Score (class Score(Turtle):):
Although the Score class is not shown in this code snippet, it's mentioned in previous discussions. It's a custom-made class responsible for tracking and displaying the player's score, as well as managing the high score.

## Overall Description:
In this game code snippet, the turtle and random modules are used as built-in Python modules to create the game's graphical interface and generate random food positions. These modules provide essential functionality for graphics and randomness in the game. The custom classes (Snake, Food, and optionally Score) are created for this game. They encapsulate game-specific logic and behaviors. The Snake class manages the snake's movements and body, the Food class handles the food item's appearance and position, and the Score class manages the scoring system. These classes are designed to work together to create the game's core functionality and interactivity.
