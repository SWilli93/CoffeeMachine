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

#TODO 1: prompt user by asking what would you like?

request = input("What would you like? ")


# TODO 2: turn off the machine by typing off

turn_on = True
turn_off = False

#TODO 3: print report


report = print(resources)
print(report)
# '''this will be to compare ingredients'''

espresso, latte, cappuccino = [menu[v]["ingredients"] for v in menu]
espresso_cost, latte_cost, cappuccino_cost = [menu[v]['cost'] for v in menu]
espresso['milk'] = 0


#TODO 4 check resources sufficient


def is_enough(request):
    global resources, espresso, latte, cappuccino
    if int(resources['water']) - int(request['water']) <= 0:
        return True
    elif resources['milk'] - request['milk'] <= 0:
        return True
    elif resources['coffee'] - request['coffee'] <= 0:
        return True
    else:
        return False

#TODO 5 Process Coins

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

#todo 6 transaction successful

def is_successful(money, drink):
    change = money - drink
    if money < drink:
        return print("insufficient funds"), False
    elif money > drink:
        answer = input("would you like change? y or n")
        if answer == 'y':
            return True, print(f"refund of ${change} incoming")
        else:
            return print("thankyou have a great day"), True
    else:
        return True, print("coffee incoming")


#todo 7: Make the coffee


if is_successful() and is_enough():
    # print(report)
    # print(new_report)


# def check_response(request):
#     global resources, resources_left
#     if request == "espresso":
#         espresso["water"] -= 50
#         espresso["coffee"] -= 18
#         return resources_left
#     elif request == "latte":
#         resources["water"] -= 200
#         resources["milk"] -= 150
#         resources["coffee"] -= 24
#         return resources
#     elif request == "cappuccino":
#         resources["water"] -= 250
#         resources["milk"] -= 100
#         resources["coffee"] -= 24
#         return resources
#     else:
#         print("Please Enter Valid Selection")
#     check_response(user_request)
#
#
# check_response(user_request)





