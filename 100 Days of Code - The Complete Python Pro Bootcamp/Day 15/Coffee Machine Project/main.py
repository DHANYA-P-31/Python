MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

def report():
    print(f"Water : {resources["water"]}ml\nMilk : {resources["milk"]}ml\nCoffee : {resources["coffee"]}g\nMoney : ${resources["money"]}")

def coff():
    while True:
        not_enough = False
        inputs = input("What would you like? (espresso/latte/cappuccino):").lower()
        if inputs == "off":
            print("Machined turned off.")
            break
        elif inputs == "report":
            report()

        elif inputs in MENU:
            for i in MENU[inputs]["ingredients"]:
                resources[i] = resources[i]- MENU[inputs]["ingredients"][i]
                if resources[i] < 0:
                    print(f"Not enough resources for {inputs},Shortage of {i}")
                    resources[i] += MENU[inputs]["ingredients"][i]
                    not_enough = True

            if not_enough:
                continue

            q = float(input("Enter no .of quarters:"))
            d = float(input("Enter no .of dimes:"))
            n = float(input("Enter no .of nickels:"))
            p = float(input("Enter no .of pennies:"))

            cost = q*0.25 + d*0.1 + n*0.05 + p*0.01

            if cost < MENU[inputs]["cost"]:
                print(f"Not enough amount The price of {inputs} is {MENU[inputs]["cost"]}")
                print(f"The ${round(cost,2)} is returned")
                continue
            else:
                resources["money"] += MENU[inputs]["cost"]
                print(f"The price of {inputs} is {MENU[inputs]["cost"]},The refunded amount {round(cost - MENU[inputs]["cost"],2)}")

            print(f"Enjoy your {inputs}")

coff()

