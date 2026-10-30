"""Data access for users and orders (SQLite)."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str


@dataclass(frozen=True)
class Order:
    id: int
    user_id: int
    total_cents: int


def connect(path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, total_cents INTEGER)"
    )
    return conn


def get_user(conn: sqlite3.Connection, user_id: int) -> User | None:
    row = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,)).fetchone()
    return User(*row) if row else None


def orders_for(conn: sqlite3.Connection, user_id: int) -> list[Order]:
    rows = conn.execute(
        "SELECT id, user_id, total_cents FROM orders WHERE user_id = ? ORDER BY id", (user_id,)
    ).fetchall()
    return [Order(*r) for r in rows]


def delete_user(conn: sqlite3.Connection, user_id: int) -> None:
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
