"""Main application for the Food Delivery System receipt generator."""

from customer import get_customer
from receipt import print_receipt


def main():
    """Collect order details and print the customer's receipt."""
    name, food, quantity, price, delivery_charges = get_customer()
    print_receipt(name, food, quantity, price, delivery_charges)


if __name__ == "__main__":
    main()
