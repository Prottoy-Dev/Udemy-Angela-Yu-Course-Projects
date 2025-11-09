# Import necessary libraries
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API token from the environment variables
TOKEN = os.getenv("TOKEN")

# Set the username associated with the Pixela account
USERNAME = "prottoy"

# Define the unique identifier for the graph
GRAPH_ID = "graph1"

# Pixela API base URL
pixela_url = "https://pixe.la/v1/users"

# Define parameters for user creation
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Construct the URL for creating a new graph
graph_url = f"{pixela_url}/{USERNAME}/graphs"

# Create headers with the user token
token = {
    "X-USER-TOKEN": TOKEN
}

# Define graph settings
graph = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "hour",
    "type": "int",
    "color": "kuro",
}

# Get the current date and time
today = datetime.now()

# Construct the URL for creating a new pixel on the graph for today's date
pixel_creation_url = f"{graph_url}/{GRAPH_ID}"

# Define data to add to the graph for today's date
graph_id = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours?"),  # User input for the quantity
}

# Send a POST request to create a new pixel on the graph
response = requests.post(url=pixel_creation_url, json=graph_id, headers=token)

# Print the response from the Pixela API
print(response.text)

# Construct the URL for updating an existing pixel for today's date
update_pixel_creation_url = f"{graph_url}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Define new data to update the existing pixel
new_graph_id = {
    "quantity": "4",  # New quantity value
}

# Construct the URL for deleting an existing pixel for today's date
delete_pixel_creation_url = f"{graph_url}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Now, let's provide additional explanations for each section of the code:

# Section 1: Importing necessary libraries.
# The script imports the required Python libraries for working with HTTP requests, dates, and environment variables.

# Section 2: Loading Environment Variables.
# It loads API credentials (TOKEN) from a .env file to keep them secure and separate from the code.

# Section 3-6: API Configuration.
# These sections define configuration parameters such as the username, graph ID, and Pixela API URL.

# Section 7: User Creation Parameters. It prepares the parameters required to create a Pixela user account,
# including the token, username, and terms of service agreement.

# Section 8-9: Creating a New Graph.
# The script constructs a URL for creating a new graph on Pixela and specifies the graph's settings.

# Section 10-12: Getting Current Date and Time.
# It retrieves the current date and time to work with timestamps for pixel creation and other operations.

# Section 13-17: Creating a New Pixel. The script constructs a URL for creating a new pixel (data point) on the graph
# for the current date. It prompts the user for input to specify the quantity of hours.

# Section 18-23: Sending a POST Request. It sends a POST request to create a new pixel on the graph using the
# provided data and authentication token. It then prints the response received from the Pixela API.

# Section 24-27: Updating a Pixel. The script constructs a URL to update an existing pixel for the current date and
# defines new data (quantity) for the update.

# Section 28-31: Deleting a Pixel.
# It constructs a URL to delete an existing pixel for the current date.

# The script essentially interacts with the Pixela API to manage data points (pixels) on a graph associated with a
# user's account.