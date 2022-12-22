from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
order_of_coffee = CoffeeMaker()
menu = Menu()

while True:
    resp = input(f"What would you like to drink? ({menu.get_items()})?").lower()
    if resp == "report":
        print(order_of_coffee.report())
    elif resp == "off":
        break
    else:
        drink = (menu.find_drink(resp))
        if drink == None:
            print(f"Sorry, {resp} is not a drink. Please enter a different "
                  f"order.")
            continue
        else:
            ingredients_available = order_of_coffee.is_resource_sufficient(drink)
            if ingredients_available == True:
                cost = drink.cost
                payment_succesful = money.make_payment(cost)
                if payment_succesful == True:
                    order_of_coffee.make_coffee(drink)
            else:
                print("Sorry, we are out of ingredients.")

