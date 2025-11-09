# Pixela-API-Interaction
This Python script interacts with the Pixela API to manage data points (pixels) on a specific graph associated with a user's Pixela account. The code performs the following actions:

## Features:
User Account Creation:

It creates a new Pixela user account with the provided API token, username, and agreement to terms of service.
## Graph Setup:

The code sets up a new graph on Pixela, defining its attributes such as the graph ID, name, unit, data type, and color.
## Pixel Creation:

Users can input the quantity (in hours) for a new data point (pixel) on the graph for the current date. The code then sends a POST request to create the pixel on the graph.
## Pixel Update:

It allows for updating an existing pixel for the current date with a new quantity value.
## Pixel Deletion:

Users can delete an existing pixel for the current date if needed.
## Prerequisites:
Before running this script, ensure you have the following:

A valid Pixela API token stored in an environment variable (TOKEN).
