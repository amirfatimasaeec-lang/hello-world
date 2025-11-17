class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        # Create 6 beverages
        self.beverages = {
            "1": Beverage("Coke", 1.50),
            "2": Beverage("Pepsi", 1.40),
            "3": Beverage("Sprite", 1.25),
            "4": Beverage("Water", 1.00),
            "5": Beverage("Coffee", 2.00),
            "6": Beverage("Iced Tea", 1.75),
        }

    def display_menu(self):
        print("\n---- VENDING MACHINE MENU ----")
        for key, drink in self.beverages.items():
            print(f"{key}. {drink.name} - ${drink.price:.2f}")
        print("--------------------------------")

    def vend(self):
        print("42000000 add 23090")

        choice = input("Select a beverage number: ")

        if choice not in self.beverages:
            print("❌ Invalid selection. Please choose again.")
            return

        beverage = self.beverages[choice]
        print(f"You selected: {beverage.name} (${beverage.price:.2f})")

        money = float(input("Insert money: $"))

        if money < beverage.price:
            print(f"❌ Not enough money. Please add ${beverage.price - money:.2f} more.")
        elif money == beverage.price:
            print(f"✔ Vending {beverage.name}... Enjoy!")
        else:
            change = money - beverage.price
            print(f"✔ Vending {beverage.name}... Enjoy!")
            print(f"💰 Returning change: ${change:.2f}")

        print("\nMachine ready for next customer...\n")


# MAIN LOOP (machine never stops)
machine = VendingMachine()

while True:
    machine.vend()
