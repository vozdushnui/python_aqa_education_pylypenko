import sys
from time import sleep


class CoffeeMachine:
    """
    Class specified for making coffee by coffee machine
    """

    def __init__(self):
        self.__water_inside_machine = 1000
        self.__milk_inside_machine = 1000
        self.__beans_inside_machine = 1000
        self.__disposable_cups_inside_machine = 3
        self.__money_inside_machine = 10
        self.__water_filler = 0
        self.__milk_filler = 0
        self.__coffee_beans_filler = 0
        self.__disposable_cups_filler = 0
        self.__coffee_machine_state = 'main_menu'
        self.__user_message = "Write action (buy, fill, take, remaining, exit):"

# defining setters \ getters for init attributes
    @property
    def coffee_machine_state(self):
        return self.__coffee_machine_state

    @coffee_machine_state.setter
    def coffee_machine_state(self, state):
        self.__coffee_machine_state = state

    @property
    def user_message(self):
        return self.__user_message

    @user_message.setter
    def user_message(self, message):
        self.__user_message = message

    @property
    def water_inside_machine(self):
        return self.__water_inside_machine

    @water_inside_machine.setter
    def water_inside_machine(self, water):
        self.__water_inside_machine = water

    @property
    def milk_inside_machine(self):
        return self.__milk_inside_machine

    @milk_inside_machine.setter
    def milk_inside_machine(self, milk):
        self.__milk_inside_machine = milk

    @property
    def beans_inside_machine(self):
        return self.__beans_inside_machine

    @beans_inside_machine.setter
    def beans_inside_machine(self, beans):
        self.__beans_inside_machine = beans

    @property
    def disposable_cups_inside_machine(self):
        return self.__disposable_cups_inside_machine

    @disposable_cups_inside_machine.setter
    def disposable_cups_inside_machine(self, disposable_cups):
        self.__disposable_cups_inside_machine = disposable_cups

    @property
    def money_inside_machine(self):
        return self.__money_inside_machine

    @money_inside_machine.setter
    def money_inside_machine(self, money):
        self.__money_inside_machine = money

    @property
    def water_filler(self):
        return self.__water_filler

    @water_filler.setter
    def water_filler(self, water):
        self.__water_filler = water

    @property
    def milk_filler(self):
        return self.__milk_filler

    @milk_filler.setter
    def milk_filler(self, milk):
        self.__milk_filler = milk

    @property
    def coffee_beans_filler(self):
        return self.__coffee_beans_filler

    @coffee_beans_filler.setter
    def coffee_beans_filler(self, beans):
        self.__coffee_beans_filler = beans

    @property
    def disposable_cups_filler(self):
        return self.__disposable_cups_filler

    @disposable_cups_filler.setter
    def disposable_cups_filler(self, cups):
        self.__disposable_cups_filler = cups

# Using a user command for the specific coffee machine state
    def action(self, user_input):
        if self.coffee_machine_state == 'main_menu':
            self.main_menu(user_input)
        elif self.coffee_machine_state == 'making_coffee':
            self.get_user_drink(user_input)
        elif self.coffee_machine_state == 'resupply_water':
            self.resupply_water(user_input)
        elif self.coffee_machine_state == 'resupply_milk':
            self.resupply_milk(user_input)
        elif self.coffee_machine_state == 'resupply_beans':
            self.resupply_beans(user_input)
        elif self.coffee_machine_state == 'resupply_cups':
            self.resupply_cups(user_input)

# defining state of the coffee machine to use next method correctly
    def set_message_for_state(self, state):
        if state == 'main_menu':
            self.user_message = "Write action (buy, fill, take, remaining, exit):"
        elif state == 'making_coffee':
            self.user_message = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 'back' - go to previous menu:"
        elif state == 'resupply_water':
            self.user_message = "Write how many ml of water you want to add:"
        elif state == "resupply_milk":
            self.user_message = "Write how many ml of milk you want to add:"
        elif state == "resupply_beans":
            self.user_message = "Write how many grams of coffee beans you want to add:"
        elif state == "resupply_cups":
            self.user_message = "Write how many disposable coffee cups you want to add:"

# actions in the 'main menu' state of the coffee machine
    def main_menu(self, user_choice):
        if user_choice == 'buy':
            self.coffee_machine_state = 'making_coffee'
            self.set_message_for_state('making_coffee')
        elif user_choice == 'fill':
            self.coffee_machine_state = 'resupply_water'
            self.set_message_for_state('resupply_water')
        elif user_choice == 'take':
            self.get_money()
        elif user_choice == 'remaining':
            self.show_remaining_ingredients()
        elif user_choice == 'exit':
            sys.exit()
        else:
            print(f"There isn't {user_choice} option. Try again, please")

# show the remaining ingredients of the coffee machine
    def show_remaining_ingredients(self):
        print(f"The coffee machine has:\n"
              f"{self.water_inside_machine} of water\n"
              f"{self.milk_inside_machine} of milk\n"
              f"{self.beans_inside_machine}of coffee beans\n"
              f"{self.disposable_cups_inside_machine} of disposable cups\n"
              f"{self.money_inside_machine} of money\n")

# cash withdrawal from the coffee machine
    def get_money(self):
        if self.money_inside_machine > 0:
            print(f"I'll gave you {self.money_inside_machine}")
            self.money_inside_machine = 0
        else:
            print("There is no money in the coffee machine")

# checking the correctness of user input for the resupply operation
    @staticmethod
    def show_filler_error(user_amount):
        if not str(user_amount).isdigit() or int(user_amount) < 0:
            print(f"You can enter only positive integer or 0. Please, try again")
            return True
        else:
            return False

# specify the amount of water to be replenished
    def resupply_water(self, user_amount):
        if cm.show_filler_error(user_amount):
            return
        else:
            self.water_filler = int(user_amount)
            self.coffee_machine_state = 'resupply_milk'
            self.set_message_for_state('resupply_milk')

# specify the amount of milk to be replenished
    def resupply_milk(self, user_amount):
        if cm.show_filler_error(user_amount):
            return
        else:
            self.milk_filler = int(user_amount)
            self.coffee_machine_state = 'resupply_beans'
            self.set_message_for_state('resupply_beans')

# specify the amount of beans to be replenished
    def resupply_beans(self, user_amount):
        if cm.show_filler_error(user_amount):
            return
        else:
            self.coffee_beans_filler = int(user_amount)
            self.coffee_machine_state = 'resupply_cups'
            self.set_message_for_state('resupply_cups')

# specify the amount of cups to be replenished
    def resupply_cups(self, user_amount):
        if cm.show_filler_error(user_amount):
            return
        else:
            self.disposable_cups_filler = int(user_amount)
            self.resupply_coffee_machine()
            self.show_remaining_ingredients()
            self.coffee_machine_state = 'main_menu'
            self.set_message_for_state('main_menu')

# resupply coffee machine with user amount of the supplies
    def resupply_coffee_machine(self):
        self.water_inside_machine += self.water_filler
        self.milk_inside_machine += self.milk_filler
        self.beans_inside_machine += self.coffee_beans_filler
        self.disposable_cups_inside_machine += self.disposable_cups_filler
        self.show_remaining_ingredients()

# make a a user-specified coffee
    def make_coffee(self, water, beans, milk, cups, money):
        if self.water_inside_machine >= water and self.milk_inside_machine >= milk and self.beans_inside_machine >= beans and self.disposable_cups_inside_machine >= cups:
            self.milk_inside_machine -= milk
            self.water_inside_machine -= water
            self.beans_inside_machine -= beans
            self.disposable_cups_inside_machine -= cups
            self.money_inside_machine += money
            self.show_making_coffee_message()
        else:
            if self.water_inside_machine < water:
                print("Sorry, not enough water")
            if self.milk_inside_machine < milk:
                print("Sorry, not enough milk")
            if self.beans_inside_machine < beans:
                print("Sorry, not enough coffee beans")
            if self.disposable_cups_inside_machine < cups:
                print("Sorry, not enough disposable cups")
                return

# make cappuccino for user
    def cappuccino(self):
        milk = 100
        water = 200
        beans = 12
        cups = 1
        money = 6
        self.make_coffee(water, beans, milk, cups, money)
        self.coffee_machine_state = 'main_menu'
        self.set_message_for_state('main_menu')

# make latte for user
    def latte(self):
        milk = 75
        water = 350
        beans = 20
        cups = 1
        money = 7
        self.make_coffee(water, beans, milk, cups, money)
        self.coffee_machine_state = 'main_menu'
        self.set_message_for_state('main_menu')

# make espresso for user
    def espresso(self):
        milk = 0
        water = 250
        beans = 16
        cups = 1
        money = 4
        self.make_coffee(water, beans, milk, cups, money)
        self.coffee_machine_state = 'main_menu'
        self.set_message_for_state('main_menu')

# specify coffee drink
    def get_user_drink(self, user_drink):
        if user_drink == 'back':
            self.coffee_machine_state = 'main_menu'
            self.set_message_for_state('main_menu')
        elif str(user_drink).isdigit():
            if int(user_drink) == 1:
                return self.espresso()
            elif int(user_drink) == 2:
                return self.latte()
            elif int(user_drink) == 3:
                return self.cappuccino()
            else:
                print(f"There is no drink with '{user_drink}' number")
        else:
            print("I don't understand you. Please, try again:")

# print some text while making coffee
    @staticmethod
    def show_making_coffee_message():
        print("Starting to make a coffee")
        sleep(1)
        print("Grinding coffee beans")
        sleep(1)
        print("Boiling water")
        sleep(1)
        print("Mixing boiled water with crushed coffee beans")
        sleep(1)
        print("Pouring coffee into the cup")
        sleep(1)
        print("Pouring some milk into the cup")
        sleep(1)
        print("Coffee is ready!")
        sleep(1)


cm = CoffeeMachine()
while True:
    response = cm.user_message
    print(cm.coffee_machine_state)
    inp = input(f"{response}\n")
    cm.action(inp)
