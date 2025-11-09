# oop-coffee-machine
# Overview:
The Coffee Machine Program is a Python script that simulates the operation of a coffee vending machine. It allows users to interact with the machine by selecting drinks from a menu, checking the machine's resources, and making payments for selected drinks.

## Components:
1. Imported Modules:

Menu: This module provides a menu of available drinks.
CoffeeMaker: The CoffeeMaker class is responsible for managing the coffee machine's resources and preparing drinks.
MoneyMachine: The MoneyMachine class handles payment processing.
2. Initialization:

coffeemaker: An instance of the CoffeeMaker class, responsible for tracking and managing the coffee machine's resources.
moneymachine: An instance of the MoneyMachine class, used for handling payments and tracking monetary transactions.
menu: An instance of the Menu class, providing access to the available drink options.
choices: A list of available drink choices retrieved from the menu.
3. Main Loop:

The program operates within a while loop controlled by the its_on variable.
Users can input their drink choices or special commands, such as "off" to turn off the machine or "report" to generate a resource report.
4. User Interaction:

Users are prompted to input their drink choice using the input function.
If the input is "off," the program exits the loop and turns off the coffee machine.
If the input is "report," the program generates and displays a resource report using coffeemaker.report().
5. Drink Selection and Payment:

If the input is a valid drink name, the program attempts to prepare the selected drink.
It first checks if there are sufficient resources available using coffeemaker.is_resource_sufficient(drink).
If resources are sufficient, it proceeds to handle payment with moneymachine.make_payment(drink.cost).
If the payment is successful, the program prepares the selected drink using coffeemaker.make_coffee(drink).
## Usage:
1. Run the program to start the coffee machine simulation.
2. Follow the on-screen prompts to select drinks and manage the machine's resources.
## Special Commands:
off: Turn off the coffee machine and exit the program.
report: Generate and display a resource report.
## Example Usage:
Input "latte" to order a latte.
Input "report" to generate a resource report.
Input "off" to turn off the coffee machine.
