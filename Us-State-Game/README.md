
# US States Guessing Game

This Python script is an educational game that challenges users to guess the names of US states by visually selecting them on a blank US map. The game is built using the Turtle graphics library for graphical display and the Pandas library for data handling.

## How It Works

The script loads a blank map of the United States.

State data, including state names and coordinates, is read from a CSV file ("50_states.csv").

The user is prompted to guess the names of US states. They can exit the game by typing "Exit."

When the user correctly guesses a state, its name is displayed on the map, and their score increases.

After the game ends, a CSV file ("not_guessed_states.csv") is generated, listing the states that were not guessed.

## Usage Instructions

Ensure the "blank_states_img.gif" and "50_states.csv" files are in the same directory as the script.

Run the script, and a window with the blank US map will appear.

Enter state names when prompted.

To exit the game, type "Exit."

After the game, check "not_guessed_states.csv" for unguessed states.

## Note: This game is designed for educational purposes, helping users learn the names and locations of US states interactively. You can change it to any country's map and its states. Just change the image file and the states.csv file.
