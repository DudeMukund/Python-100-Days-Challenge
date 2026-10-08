import os
from art import logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

is_coffee_macine_on = True
while is_coffee_macine_on:
    clear()
    print(logo)

    choose = input(f"What would you like? {menu.get_items()}:").lower()

    if choose =="off":
        is_coffee_macine_on = False
    elif choose =="report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(choose):
        drink = menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    input("\nPress Enter to continue...")

        