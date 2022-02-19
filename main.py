import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


c_machine = CoffeeMaker()
c_menu = Menu()
c_money = MoneyMachine()

#print(c_menu.menu[0])

isOn = True

while isOn:
    mcom = input("What would you like? (espresso/latte/cappuccino): ")

    if mcom == "off":
        isOn = False
    elif mcom == "report":
        print(c_machine.report())
        print(c_money.report())
    elif c_menu.find_drink(mcom) == None:
        pass
    else:
        chosen_drink = c_menu.find_drink(mcom)
        if c_machine.is_resource_sufficient(chosen_drink) == True:
            cost = chosen_drink.cost
            c_money.make_payment(cost)
            c_machine.make_coffee(chosen_drink)


