"""Prices are integers in cents everywhere, never floats."""

from __future__ import annotations


def apply_discount(total_cents: int, percent: int) -> int:
    """Total after a percentage discount, rounded down to the cent."""
    if not 0 <= percent <= 100:
        raise ValueError(f"discount must be 0-100, got {percent}")
    return total_cents * (100 - percent) // 100


def order_total(item_prices_cents: list[int], shipping_cents: int = 0) -> int:
    if any(p < 0 for p in item_prices_cents):
        raise ValueError("item prices cannot be negative")
    return sum(item_prices_cents) + shipping_cents


def apply_coupon(total_cents: int, code: str) -> int:
    """Apply a coupon code to an order total."""
    code = code.strip().upper()
    if code == "WELCOME10":
        return apply_discount(total_cents, 10)
    if code == "FREESHIP" and total_cents >= 50_000:
        return total_cents - 4_900
    if code.startswith("STAFF-"):
        return apply_discount(total_cents, 30)
    return total_cents
