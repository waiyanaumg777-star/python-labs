"""Pytest tests for the FoodExpress order calculator."""

import pytest

from food_order import calculate_total


def test_order1():
    assert calculate_total(10, 2) == 20


def test_total_is_30():
    assert calculate_total(10, 3) == 30


def test_total_is_100():
    assert calculate_total(20, 5) == 100


def test_total_is_10():
    assert calculate_total(5, 2) == 10


def test_invalid_price_text():
    with pytest.raises(ValueError, match="Invalid price"):
        calculate_total("invalid price", 2)


def test_invalid_quantity_text():
    with pytest.raises(ValueError, match="Invalid quantity"):
        calculate_total(10, "invalid quantity")


def test_zero_or_negative_price_is_rejected():
    with pytest.raises(ValueError, match="Invalid price"):
        calculate_total(0, 2)
    with pytest.raises(ValueError, match="Invalid price"):
        calculate_total(-5, 2)


def test_zero_or_negative_quantity_is_rejected():
    with pytest.raises(ValueError, match="Invalid quantity"):
        calculate_total(10, 0)
    with pytest.raises(ValueError, match="Invalid quantity"):
        calculate_total(10, -1)
