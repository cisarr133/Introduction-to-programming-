class Item:
    def __init__(self, code, name, price, category, stock):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock


class VendingMachine:
    def __init__(self):
        self.items = [
            Item("01", "Coffee", 2.50, "Drink", 5),
            Item("02", "Tea", 2.00, "Drink", 5),
            Item("03", "Chocolate Bar", 1.50, "Snack", 5),
            Item("04", "Biscuits", 1.20, "Snack", 5)
        ]

    def display_menu(self):
        print("\n--- VENDING MACHINE MENU ---")
        for item in self.items:
            print(f"{item.code} | {item.name} (£{item.price:.2f}) | {item.category} | Stock: {item.stock}")

    def get_item_by_code(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def suggest_item(self, purchased_item):
        if purchased_item.name == "Coffee":
            print("Suggestion: Would you like some Biscuits to go with your Coffee?")

    def run(self):
        balance = 0.0
        while True:
            try:
                balance += float(input("Insert money (£): "))
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        while True:
            self.display_menu()
            choice = input("Enter item code to buy (or Q to quit): ").upper()
            if choice == "Q":
                break

            item = self.get_item_by_code(choice)
            if item is None:
                print("Invalid item code.")
                continue

            if item.stock <= 0:
                print("Sorry, this item is out of stock.")
                continue

            if balance < item.price:
                print("Insufficient funds.")
                more = input("Insert more money? (Y/N): ").strip().upper()
                if more == "Y":
                    try:
                        balance += float(input("Insert money (£): "))
                    except ValueError:
                        print("Invalid amount.")
                continue

            balance -= item.price
            item.stock -= 1
            print(f"{item.name} has been dispensed.")
            self.suggest_item(item)
            print(f"Remaining balance: £{balance:.2f}")

        print(f"Change returned: £{balance:.2f}")
        print("Thank you for using the vending machine!")


machine = VendingMachine()
machine.run()