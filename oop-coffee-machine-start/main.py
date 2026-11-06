from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coff():
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()

    while True:
        inputs = input(f"What would you like? ({menu.get_items()}):").lower()
        if inputs == "off":
            print("Machined turned off.")
            break
        elif inputs == "report":
            coffee.report()
            money.report()

        else:
            item = menu.find_drink(inputs)
            cost = 0
            if coffee.is_resource_sufficient(item) and money.make_payment(cost):
                coffee.make_coffee(item)

coff()