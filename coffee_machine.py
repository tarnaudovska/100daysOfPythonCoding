logo = "☕ machine"

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

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def has_resources(coffee):
    resources_enough = True
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            resources_enough = False

    return resources_enough

def resources_deduction(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
        #print(f"From the {ingredient} resources we deducted the {ingredient} needed for the {coffee}. Now you have {resources[ingredient]} left")  

def coffe_ingredients(coffee, ingredient):
    return MENU[coffee]["ingredients"][ingredient]

def process_coins():
    """Returns the total calculated from coins inserted"""
    total = 0.0
    print("Insert coints.")
    total = int(input("how many quarters?: ")) * 0.25 
    total += int(input("how many dimes?: ")) * 0.1 
    total += int(input("how many nickles?: ")) * 0.05 
    total += int(input("how many pennies?: ")) * 0.01 

    return total

def is_transaction_successful(money_recieved, drink):
    """Return True when the payment is accepted, or False if money is insuficient"""
    if money_recieved >= MENU[drink]["cost"]:
        change = round(money_recieved - MENU[drink]["cost"], 2)
        print(f"Here is your {drink} and you have {change}$ change\nThank you for using this coffee machine")
        global profit 
        profit += MENU[drink]["cost"]
        return True
    else:
        print(f'Sorry that\'s not enough money. Money refund. {money_recieved} are not enough. The coffee costs {MENU[drink]["cost"]}$')
        return False

print(f'Welcome to the {logo}')

is_machine_on = True
while is_machine_on:
    promt = input('What would you like? Espresso,latte or cappuccino?').lower() 
    if promt == "espresso" or promt == "cappuccino" or promt == "latte":
        print("Please pay for the coffee")
        
        if has_resources(promt) == True and is_transaction_successful(process_coins(), promt) == True:
            resources_deduction(promt)
            print(f'There are: {resources["water"]}ml of water, {resources["milk"]}ml of milk and {resources["coffee"]}g of coffee left')
        else:
            print("Not sufficient resources or money")
    elif promt == "report":
        print(f"Current resource values are:\nCoffee: {resources['coffee']}g\nWater: {resources['water']}ml\nMilk: {resources['milk']}\nMoney: {profit}\n")
    elif promt == "off":
        is_machine_on = True
        break
    else:
        print("That is not a choice")