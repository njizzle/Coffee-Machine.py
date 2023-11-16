from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

print("Welcome to the Coffee Shop!")
while True:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        break
    elif choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
                print("Here is your {}. Enjoy!" .format(drink))

            else:
                print("Sorry, you don't have enough money.")
                
            
        
        else:
            print("Sorry, we don't have enough resources to make that drink.")
            
        
    