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

# user_request = input("What would you like? ")
# if user_request:
#     print("Ok here you go.")
# else:
#     print("machine is off")

# TODO 2: turn off the machine by typing off

turn_on = True
turn_off = False

#TODO 3: print report

# if *arg == report:
#     report = print(resources)

'''this will be to compare ingredients'''
espresso, latte, cappuccino = [menu[v] for v in menu]
print(espresso)



# for resources["amount"] in resources:
#     if "amount" < drink:
#         print("sorry inefficient amount of resources")
#     else:
#         print("ok here you go")


# def check_response(request):
#     global resources, user_request
#     if request == "espresso":
#         resources["water"] -= 50
#         resources["coffee"] -= 18
#         return resources
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


# check_response(user_request)





