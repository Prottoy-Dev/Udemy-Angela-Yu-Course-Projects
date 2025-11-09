# Import necessary modules
from turtle import Turtle, Screen  # Turtle for graphics, Screen for creating the game window
import pandas  # Pandas for data manipulation

# Create a Turtle graphics window and set its dimensions
tv = Screen()
tv.setup(750, 500)

# Load the image of the blank US map
tv.addshape("blank_states_img.gif")
image = "blank_states_img.gif"
timmy = Turtle(image)  # Create a Turtle to display the map
game_on = True  # Initialize the game state variable
score = 0  # Initialize the user's score
data = pandas.read_csv("50_states.csv")  # Load state data from a CSV file into a Pandas DataFrame
state_list = data.state.to_list()  # Create a list of all US states from the DataFrame
guess_states = []  # Create an empty list to store guessed states

# Start the game loop
while game_on:
    # Prompt the user to enter a state name
    answer = tv.textinput(title=f"{score}/50 States Correct", prompt="What's the state?")

    # Check if the user wants to exit the game
    if answer is None or answer.lower() == "exit":
        game_on = False  # Exit the game loop
    else:
        answer = answer.title()  # Convert the user's input to title case

    # Iterate through the list of all states to check if the user's answer is correct
    for state in state_list:
        if answer == state:
            if answer not in guess_states:  # Check if the state has not been guessed before
                guess_states.append(answer)  # Add the correct guess to the list
                t = Turtle()
                t.hideturtle()
                t.penup()
                score += 1  # Increment the score
                state_data = data[data.state == answer]  # Get data for the guessed state from the DataFrame
                t.goto(int(state_data.x), int(state_data.y))  # Move the Turtle to the state's location on the map
                t.write(answer)  # Display the state name on the map

# Create a list of states that were not guessed
not_guessed_states = [state for state in state_list if state not in guess_states]

# Create a new Pandas DataFrame for the not guessed states
learn = pandas.DataFrame(not_guessed_states)

# Save the list of not guessed states to a CSV file
learn.to_csv("not_guessed_states.csv")
# print(not_guessed_states)
