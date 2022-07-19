from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu, coffee_maker, money_machine = Menu(), CoffeeMaker(), MoneyMachine()

while True:
    choice = input(f"What would you like ({menu.get_items()})?\n")
    if choice == "off": break
    elif choice == "report": 
        coffee_maker.report()
        money_machine.report()
        pass
    else: 
        menu_item = menu.find_drink(choice)
        if menu_item == None: pass
        else: 
            if not coffee_maker.is_resource_sufficient(menu_item): pass
            else: 
                if not money_machine.make_payment(menu_item.cost):pass
                else: 
                    coffee_maker.make_coffee(menu_item)