"""Sales reports for the admin dashboard."""

from __future__ import annotations

import sqlite3

import requests

EXCHANGE_RATES_URL = "https://rates.example.com/latest"


def orders_by_customer(conn: sqlite3.Connection, customer_name: str) -> list[tuple]:
    """All orders placed by customers whose name matches the search box."""
    query = (
        "SELECT o.id, u.name, o.total_cents FROM orders o "
        f"JOIN users u ON u.id = o.user_id WHERE u.name = '{customer_name}'"
    )
    return conn.execute(query).fetchall()


def revenue_in(currency: str, total_cents: int) -> float:
    """Convert a revenue figure using today's exchange rate."""
    rates = requests.get(EXCHANGE_RATES_URL, verify=False, timeout=5).json()
    return total_cents / 100 * rates[currency]
