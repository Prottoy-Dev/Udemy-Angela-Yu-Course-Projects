# Import necessary modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the CoffeeMaker, MoneyMachine, and Menu classes
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

# Retrieve the list of available drink choices from the Menu class
choices = menu.get_items()

# Initialize the main loop control variable
its_on = True

# Main program loop
while its_on:
    # Prompt the user to select a drink or enter a special command
    ask = input(f"What would you like? ({choices}): ")

    # Check for the "off" command to turn off the coffee machine and exit
    if ask == "off":
        its_on = False
    # Check for the "report" command to generate and display a resource report
    elif ask == "report":
        print(coffeemaker.report())
    else:
        # Attempt to find the selected drink in the menu
        drink = menu.find_drink(ask)

        # Check if there are sufficient resources to prepare the selected drink
        if coffeemaker.is_resource_sufficient(drink):
            # Attempt to process payment for the selected drink
            if moneymachine.make_payment(drink.cost):
                # If payment is successful, prepare and serve the drink
                coffeemaker.make_coffee(drink)
