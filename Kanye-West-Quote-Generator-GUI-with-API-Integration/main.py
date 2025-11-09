# Import necessary modules
from tkinter import *
import requests


# Function to fetch a Kanye West quote using an API
def get_quote():
    # Send a GET request to the Kanye Rest API
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()  # Raise an exception if the request was not successful
    data = response.json()  # Parse the response JSON data

    # Update the text in the canvas with the retrieved Kanye West quote
    canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", 20, "bold"))


# Create a Tkinter window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas widget for displaying the background image and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create a button widget with Kanye's image to trigger fetching a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter main event loop
window.mainloop()
