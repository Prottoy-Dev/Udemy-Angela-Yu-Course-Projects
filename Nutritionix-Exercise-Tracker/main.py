# Import necessary libraries and modules
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API credentials and endpoints from environment variables
app_id = os.getenv("NT_APP_ID")
app_key = os.getenv("NT_APP_KEY")
nutriotionix_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4180e1e5035bdd66ed5dd54ffcc31cca/myWorkouts/workouts"
Bearer_YOUR_TOKEN = os.getenv("TOKEN")

# Define user information (can be customized)
weight = 57
gender = "male"
height = 160
age = 25

# Prompt the user to input an exercise
query = input("What exercise did you do? ")

# Define headers for the Nutritionix API request
headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

# Define parameters for the Nutritionix API request
parameters = {
    "query": query,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

# Send a POST request to the Nutritionix API to get exercise information
response = requests.post(url=nutriotionix_endpoints, json=parameters, headers=headers)
response.raise_for_status()

# Define bearer headers for the Sheety API request
bearer_headers = {
    "Authorization": Bearer_YOUR_TOKEN
}

# Get the current date and time
today = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%X")

# Loop through the exercises returned by the Nutritionix API
for exercise in response.json()["exercises"]:
    # Prepare workout data
    workout_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Send a POST request to the Sheety API to log the workout data
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=workout_data,
        headers=bearer_headers
    )

    # Print the response from the Sheety API
    print(sheet_response.text)