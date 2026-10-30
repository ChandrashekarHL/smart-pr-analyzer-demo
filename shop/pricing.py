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


def split_evenly(total_cents: int, parts: int) -> list[int]:
    """Split a total into `parts` amounts that differ by at most one cent and
    add up exactly to the total (the first ones get the extra cents)."""
    if parts <= 0:
        raise ValueError(f"parts must be positive, got {parts}")
    if total_cents < 0:
        raise ValueError("total cannot be negative")
    base, extra = divmod(total_cents, parts)
    return [base + 1 if i < extra else base for i in range(parts)]
