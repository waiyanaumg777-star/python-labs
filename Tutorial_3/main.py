# main.py
# Main program for the cafe billing system.

from utils import calculate_total, print_receipt


def get_quantity(item_name):
    """Ask for a non-negative whole-number quantity."""
    while True:
        try:
            quantity = int(input(f"{item_name} quantity: "))
            if quantity < 0:
                print("Please enter zero or a positive whole number.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("===== CAFE BILLING SYSTEM =====")

    customer_name = input("Customer name: ").strip()
    while not customer_name:
        print("Customer name cannot be empty.")
        customer_name = input("Customer name: ").strip()

    coffee_qty = get_quantity("Coffee")
    tea_qty = get_quantity("Tea")
    sandwich_qty = get_quantity("Sandwich")

    total = calculate_total(coffee_qty, tea_qty, sandwich_qty)
    print_receipt(
        customer_name,
        coffee_qty,
        tea_qty,
        sandwich_qty,
        total
    )


if __name__ == "__main__":
    main()
