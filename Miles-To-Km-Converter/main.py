"""
Mile to Kilometer Converter

This is a simple graphical application that converts distances from miles to kilometers using the tkinter library.

Usage:
1. Enter the distance in miles in the input field.
2. Click the "Calculate" button to convert the distance to kilometers.
3. The converted value will be displayed on the screen.

"""

# Import the tkinter library, which provides the graphical user interface components.
from tkinter import *


# Function to perform the conversion when the "Calculate" button is clicked.
def calculate():
    # Retrieve the value entered in the input field as a float.
    miles_value = float(entry.get())

    # Perform the conversion from miles to kilometers and round the result.
    km_value = round(miles_value * 1.609)

    # Create a Label widget to display the result and place it on the window.
    ans = Label(text=km_value)
    ans.grid(column=1, row=1)


# Create the main application window.
window = Tk()
window.title("Mile to Km Converter")

# Configure padding for the entire window.
window.config(padx=20, pady=20)

# Create an Entry widget for user input.
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Create labels to describe the input and output fields.
miles = Label(text="Miles")
miles.grid(column=2, row=0)

label = Label(text="is equals to")
label.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

# Create a button that triggers the calculation when clicked.
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Start the tkinter event loop to display the GUI and handle user interactions.
window.mainloop()
