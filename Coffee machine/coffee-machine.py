class CoffeeMachine:

    def __init__(self):
        self.available_water = 400
        self.available_milk = 540
        self.available_beans = 120
        self.available_cup = 9
        self.money = 550

    def initial_state(self):
        print("The coffee machine has:")
        print(self.available_water, "of water")
        print(self.available_milk, "of milk")
        print(self.available_beans, "of coffee beans")
        print(self.available_cup, "of disposable cups")
        print("$", self.money, "of money")

    def latte(self):

        if self.available_water < 350:
            print("Sorry, not enough water!")

        if self.available_milk < 75:
            print("Sorry, not enough milk!")

        if self.available_beans < 20:
            print("Sorry, not enough coffee beans")

        if self.available_cup < 1:
            print("Sorry, not enough disposable cups")

        if self.available_water >= 350 and self.available_milk >= 75 and self.available_beans >= 20 and self.available_cup >= 1:
            self.available_water -= 350
            self.available_milk -= 75
            self.available_beans -= 20
            self.available_cup -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")

    def cappuccino(self):

        if self.available_water < 200:
            print("Sorry, not enough water!")

        if self.available_milk < 100:
            print("Sorry, not enough milk!")

        if self.available_beans < 12:
            print("Sorry, not enough coffee beans")

        if self.available_cup < 1:
            print("Sorry, not enough disposable cups")

        if self.available_water >= 200 and self.available_milk >= 100 and self.available_beans >= 12 and self.available_cup >= 1:
            self.available_water -= 200
            self.available_milk -= 100
            self.available_beans -= 12
            self.available_cup -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")

    def espresso(self):

        if self.available_water < 250:
            print("Sorry, not enough water!")

        if self.available_beans < 16:
            print("Sorry, not enough coffee beans")

        if self.available_cup < 1:
            print("Sorry, not enough disposable cups")

        if self.available_water >= 250 and self.available_beans >= 16 and self.available_cup >= 1:
            self.available_water -= 250
            self.available_beans -= 16
            self.available_cup -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")

    def menu(self):

        while True:
            choice = input("Write action (buy, fill, take, remaining, exit):")

            if choice == "buy":
                coffee_type = input(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if coffee_type == "1":
                    self.espresso()

                elif coffee_type == "2":
                    self.latte()

                elif coffee_type == "3":
                    self.cappuccino()

                elif coffee_type == "back":
                    continue

                else:
                    print()

            elif choice == "fill":
                water_add = int(input("Write how many ml of water do you want to add:"))
                milk_add = int(input("Write how many ml of milk do you want to add:"))
                beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
                cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.available_water += water_add
                self.available_milk += milk_add
                self.available_beans += beans_add
                self.available_cup += cups_add

            elif choice == "take":
                print("I gave you $", self.money)
                self.money = 0

            elif choice == "remaining":
                self.initial_state()

            elif choice == "exit":
                break

            else:
                print()


tasty = CoffeeMachine()
tasty.menu()
