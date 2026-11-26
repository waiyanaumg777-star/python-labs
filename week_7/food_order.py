"""Calculation and validation functions for FoodExpress orders."""

import math


def calculate_total(price, quantity):
    """Calculate an order total after validating price and quantity.

    Args:
        price: Price per item in RM. Must be a positive finite number.
        quantity: Number of items. Must be a positive whole number.

    Returns:
        The total price as a float.

    Raises:
        ValueError: If price or quantity is invalid.
    """
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("Invalid price")
    if not math.isfinite(price) or price <= 0:
        raise ValueError("Invalid price")

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise ValueError("Invalid quantity")
    if quantity <= 0:
        raise ValueError("Invalid quantity")

    return price * quantity
