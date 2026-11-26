# utils.py
# Functions used by the cafe billing program.

# Prices are in Malaysian Ringgit (RM).
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee, tea, sandwich):
    """Return the total bill based on item quantities."""
    total = (
        coffee * COFFEE_PRICE
        + tea * TEA_PRICE
        + sandwich * SANDWICH_PRICE
    )
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    """Print the customer's receipt."""
    print("\n===== RECEIPT =====")
    print(f"Customer : {customer_name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-------------------")
    print(f"Total = RM {total:.2f}")
