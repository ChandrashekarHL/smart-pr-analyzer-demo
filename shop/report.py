"""Customer spend report for the admin page."""

from __future__ import annotations

from shop.db import Order


def unique_customers(orders: list[Order]) -> list[int]:
    seen = []
    for order in orders:
        if order.user_id not in seen:
            seen.append(order.user_id)
    return seen


def spend_by_customer(orders: list[Order]) -> dict[int, int]:
    report = {}
    for user_id in unique_customers(orders):
        total = 0
        for order in orders:
            if order.user_id == user_id:
                total += order.total_cents
        report[user_id] = total
    return report
