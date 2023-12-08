from menu import MENU, money, resources


def check_resource(drink_type_param):
    for item in resources:
        if resources[item] < MENU[drink_type_param]['ingredients'][item]:
            print(f'Sorry there is not enough {item}')
            return False
        else:
            resources[item] = resources[item] - MENU[drink_type_param]['ingredients'][item]
            return True


def process_coins(drink_type_param):
    """returns the money for the coffee"""
    total = 0
    print("please insert coins: ")
    total += int(input('how many quarters?: '))*0.25
    total += int(input('how many dimes?: '))*0.1
    total += int(input('how many nickles?: '))*0.05
    total += int(input('how many nickles?: '))*0.01
    cost = MENU[drink_type_param]['cost']
    if total >= cost:
        if total - cost > 0:
            print("Here is $", total-cost, 'in change')
        print(f'Here is your {drink_type_param} ☕. Enjoy!')
        return cost
    else:
        print("Sorry that is not enough money. Money refunded.")


should_continue = True
while should_continue:
    drink_type = input("What would you like? (espresso/latte/ cappuccino): ").lower()
    if drink_type == 'report':
        print(f"Water: {resources['water']}ml \n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: {money}")
    elif drink_type == 'off':
        should_continue = False
    else:
        if check_resource(drink_type):
            money += process_coins(drink_type)
  