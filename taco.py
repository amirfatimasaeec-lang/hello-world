# --- 1. The Program's Memory (Variables and Lists) ---
# This list will save the names of the food items you order.
order_items = []
# This variable will save the total money you owe. We start it at zero.
total_due = 0.0

# This "dictionary" acts as our menu. It stores the item number, name, and price.
menu = {
    1: {"item": "Taco", "price": 2.50},
    2: {"item": "Burrito", "price": 4.75},
    3: {"item": "Nachos", "price": 6.20},
    4: {"item": "Soft Drink", "price": 2.00},
    5: {"item": "Quit", "price": 0.00}  # Quit option has no price
}


# --- 2. The Menu Printer (A Function) ---
def display_menu():
    """This function just prints the menu, so we don't have to type it out multiple times."""
    print("\n" + "=" * 20)
    print("  Taco Palace Menu")
    print("=" * 20)
    # This loop goes through every item in our 'menu' memory and prints it.
    for num, details in menu.items():
        if num != 5:
            print(f"{num}. {details['item']:<10} (${details['price']:.2f})")
        else:
            print(f"{num}. {details['item']}")
    print("-" * 20)


# --- 3. The Main Ordering Loop ---
def start_ordering_system():
    """This is the main part of the program that runs everything."""

    # We need to be able to change our total_due and order_items from inside this function.
    global total_due
    global order_items

    # Welcome message!
    print("🌮 Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")

    # We use a 'while' loop to keep the program running until we tell it to stop.
    ordering = True
    while ordering:

        # 1. Show the menu
        display_menu()

        # 2. Get the user's choice
        try:
            # We ask the user to type a number and try to save it as an integer (a whole number).
            user_input = int(input("Enter your selection (1-5): "))
        except ValueError:
            # If they type "hello" instead of a number, we catch the error.
            print("\n❌ That's not a number. Please enter a number from 1 to 5.")
            continue  # This goes back to the start of the 'while' loop.

        # 3. Check the choice using 'if-else'

        if user_input == 5:
            # The user selected 5, so we set 'ordering' to False.
            ordering = False
            # When the loop checks itself again, it will stop because 'ordering' is False.

        elif user_input in menu:
            # The user picked a number that is a real item (1, 2, 3, or 4).

            # Look up the item's name and price from our 'menu' memory.
            item_details = menu[user_input]
            item_name = item_details['item']
            item_price = item_details['price']

            # ⭐️ Update the list and the total!
            order_items.append(item_name)  # Add the name to our list
            total_due += item_price  # Add the price to the total

            print(f"\n✅ You selected a {item_name}. Price: ${item_price:.2f}. Running Total: ${total_due:.2f}")

        else:
            # The user typed a number like 6 or 100.
            print("\n❌ Invalid selection. Please enter a number from 1 to 5.")

    # --- 4. Conclusion (After the loop stops) ---
    print("\n" + "=" * 40)
    print("🛑 Thank you for ordering from Taco Palace!")

    if order_items:  # Checks if the list has any items in it

        # This part just makes the list of items look nice (e.g., "a Taco and a Burrito").
        item_list_str = ", ".join(order_items)

        print(f"🎉 You ordered: {item_list_str}.")
        print(f"💰 Your final total is: ${total_due:.2f}")
    else:
        print("You did not order any items. Goodbye!")
    print("=" * 40 + "\n")


# Start the program!
start_ordering_system()