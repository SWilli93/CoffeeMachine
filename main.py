menu = {
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#COFFEE MACHINES

espresso, latte, cappuccino = [menu[v]["ingredients"] for v in menu]
espresso_cost, latte_cost, cappuccino_cost = [menu[v]['cost'] for v in menu]
espresso['milk'] = 0
variable = ''
request = input("What would you like? ")
drink_cost = ''
new_resources = {}


def what_is(user_request):
    global drink_cost
    if user_request == 'espresso':
        drink_cost = espresso_cost
        return espresso, drink_cost
    elif user_request == 'latte':
        drink_cost = latte_cost
        return latte, drink_cost
    elif user_request == 'cappuccino':
        drink_cost = cappuccino_cost
        return cappuccino, drink_cost
    elif user_request == 'report':
        return resources, print(resources)
    elif user_request == 'off':
        return print('powering off')
    else:
        print("Please enter proper selection")
        return False


def enough_resources(order):
    orders = order[0]
    if resources['water'] - orders['water'] >= 0 and resources['milk'] - orders['milk'] >= 0 and resources['coffee'] - orders['coffee'] >= 0:
        new_resources['water'] = resources['water'] - orders['water']
        new_resources['milk'] = resources['milk'] - orders['milk']
        new_resources['coffee'] = resources['coffee'] - orders['coffee']
        return True, new_resources
    else:
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_successful(user_money, order):
    change = user_money - order
    if user_money < order:
        return print("insufficient funds"), False
    elif user_money > order:
        answer = input("would you like change? y or n: ")
        if answer == 'y':
            return True, print(f"refund of ${change} incoming")
        else:
            user_money += change
            return print("We appreciate your donation, standby for coffee"), True, user_money
    else:
        return True, print("coffee incoming")


drink = what_is(request)
if drink != False:
    is_on = True
    money = process_coins()
    while is_on and is_successful(money, drink_cost) and enough_resources(drink):
        print(resources)
        print(new_resources)
        print(money)
        print('Enjoy your Coffee!')
        break



















