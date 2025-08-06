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
}

profit = 0

def modify_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if drink!="espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    for item in resources:
        if resources[item]<0:
            print(f"Sorry there is not enough {item}")
            return 0
    return 1

def money(quarter,dime,nickle,penny,drink):
    total_amount = quarter*0.25 + dime*0.1 + nickle*0.05 + penny*0.01
    if total_amount >= MENU[drink]["cost"]:
        change=round(total_amount-MENU[drink]["cost"],2)
        print(f"Here is {change} in change")
        print(f"Here is your {drink} ☕️. Enjoy!")
        global profit
        profit += MENU[drink]["cost"]
        return 1
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

def coffee_machine():
    is_on = True
    while is_on:
        drink=input("What would you like?(espresso/latte/cappuccino):")
        if drink=="off":
            is_on = False
        elif drink=="report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif modify_resources(drink):
            quarters=int(input("How many quarters?:"))
            dimes=int(input("How many dimes?:"))
            nickles=int(input("How many nickles?:"))
            pennies=int(input("How many pennies?:"))
            if money(quarters,dimes,nickles,pennies,drink):
                coffee_machine()
            else:
                resources["water"] += MENU[drink]["ingredients"]["water"]
                resources["milk"] += MENU[drink]["ingredients"]["milk"]
                resources["coffee"] += MENU[drink]["ingredients"]["coffee"]

coffee_machine()                
