"""Prices are integers in cents everywhere, never floats."""

from __future__ import annotations


def apply_discount(total_cents: int, percent: int) -> int:
    """Total after a percentage discount, rounded down to the cent."""
    if total_cents < 0:
        raise ValueError("total cannot be negative")
    if not 0 <= percent <= 100:
        raise ValueError(f"discount must be 0-100, got {percent}")
    return total_cents * (100 - percent) // 100


def order_total(item_prices_cents: list[int], shipping_cents: int = 0) -> int:
    if shipping_cents < 0:
        raise ValueError("shipping cannot be negative")
    if any(p < 0 for p in item_prices_cents):
        raise ValueError("item prices cannot be negative")
    return sum(item_prices_cents) + shipping_cents
