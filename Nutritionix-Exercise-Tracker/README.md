# nutritionix-exercise-tracker
This Python script helps users track their workouts by logging exercise details and retrieving exercise-related data from external APIs.

## Overview

Workout Tracker is a Python script designed to simplify the process of tracking workouts. It interacts with two external APIs: Nutritionix and Sheety. Users input the exercise they've completed, and the script fetches exercise-related data from Nutritionix, including exercise duration and calories burned. It then logs this information using the Sheety API, helping users maintain a record of their workouts.

## Usage

1. Set up your environment:
   - Create a `.env` file with the necessary API credentials and endpoints (Nutritionix and Sheety).
   - Customize your personal information (weight, gender, height, age) in the script to match your profile.

2. Run the script:
   - Execute the Python script, and it will prompt you to input the exercise you've just completed.

3. Review the results:
   - The script will retrieve exercise data from Nutritionix and log your workout using the Sheety API.
   - The response from the Sheety API will be printed, allowing you to see the details of your recorded workout.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:
- Submit issues for bug reports or feature requests.
- Fork the repository, create a branch for your changes, and submit a pull request.
- Adhere to coding standards and conventions.
