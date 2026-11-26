"""Collect and validate customer order information."""


def get_customer():
    """Return customer name, food, quantity, unit price and delivery charge."""
    print("=== Customer Information ===")

    name = input("Customer Name: ").strip()
    while not name:
        print("Customer name cannot be empty.")
        name = input("Customer Name: ").strip()

    while True:
        food = input("Food Ordered (Cake/Muffin): ").strip().capitalize()
        if food in ("Cake", "Muffin"):
            break
        print("Please enter Cake or Muffin.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a whole-number quantity.")

    while True:
        try:
            price = float(input("Price per Item (RM): "))
            if price > 0:
                break
            print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid price.")

    while True:
        delivery_choice = input("Delivery (Y/N): ").strip().upper()
        if delivery_choice in ("Y", "N"):
            break
        print("Please enter Y or N.")

    delivery_charges = 5.00 if delivery_choice == "Y" else 0.00

    return name, food, quantity, price, delivery_charges
