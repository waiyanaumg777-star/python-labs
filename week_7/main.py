"""Main program for the FoodExpress order calculator."""

from food_order import calculate_total


def main():
    """Collect order details, validate them, and display the payment."""
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
        total = calculate_total(price, quantity)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Total Payment = RM {total:.2f}")


if __name__ == "__main__":
    main()
