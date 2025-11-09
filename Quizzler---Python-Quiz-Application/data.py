import requests

# Make an API request to retrieve trivia questions
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

# Check for HTTP request status
response.raise_for_status()

# Parse the JSON response to extract the trivia questions
question_data = response.json()["results"]

# The 'question_data' variable now contains a list of trivia questions
