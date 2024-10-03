# Coffee Machine Project
# Problem Statement-
# Basically it will ask user espresso, latte, cappuccino and report
# then the user will input what he wants
# resources will be checked
# If resources are sufficient the money will be asked
# if the money is over the coffee amount it will be refunded
# if everything goes right the user will get his coffee
# For espresso - 50mlWater, 18g coffee,
# For Latte = 200mlWater, 24g coffee, 150ml milk
# For cappuccino = 250mlWater, 24g coffee, 100ml milk.
# penny=1c,Nickel=5C,Dime=10C,Quarter=25C
# Money for all three is 2.5, 3.5, 4 respectively.
# Initially, it will be 2000ml Water, 300g coffee, 1500ml milk.
# Let's Build!

options = ["1.Espresso", "2.Latte", "3.Cappuccino", "4.Data & Prices"]
esp = {'water': 50, 'coffee': 18, 'price': 2.5, 'name': "Espresso"}
lat = {'water': 200, 'coffee': 24, 'milk': 150, 'price': 3.5, 'name': "Latte"}
cap = {'water': 250, 'coffee': 18, 'milk': 100, 'price': 4.0, 'name': "Cappuccino"}
init = {'water': 2000, 'coffee': 300, 'milk': 1000, 'money': 0}

def execute(inp):
    if inp == 4:
        print_dict()
    else:
        get_coffee(inp)

def print_dict():
    getDetails("Machine-Details", init)
    getDetails("Latte", lat)
    getDetails("Cappuccino", cap)
    getDetails("Espresso", esp)

def getDetails(title, details):
    print(f"\n{title}")
    for k, v in details.items():
        print(f"{k.capitalize()}: {v}")

def get_coffee(opt):
    coffee = [esp, lat, cap][opt - 1]
    if not check_resources(coffee):
        print("Sorry! Not enough resources.")
        return
    if not get_money(coffee):
        print("Sorry! Not enough money.")
        return
    print(f"Enjoy your {coffee['name']}!")
    update_resources(coffee)

def check_resources(coffee):
    for key in coffee:
        if key != 'price' and key != 'name' and coffee[key] > init[key]:
            return False
    return True

def get_money(coffee):
    pen = int(input("Enter the pennies: "))
    nic = int(input("Enter the nickels: "))
    dim = int(input("Enter the dimes: "))
    qua = int(input("Enter the quarters: "))
    total_money = pen * 0.01 + nic * 0.05 + dim * 0.10 + qua * 0.25

    if total_money >= coffee['price']:
        change = round(total_money - coffee['price'], 2)
        print(f"Here is your change: ${change}")
        init['money'] += coffee['price']
        return True
    else:
        return False

def update_resources(coffee):
    for key in coffee:
        if key != 'price' and key != 'name':
            init[key] -= coffee[key]

print("Welcome to the Coffee Machine")
print("What will you have?")
for option in options:
    print(option)

n = int(input("Enter the number for your choice: "))
execute(n)
