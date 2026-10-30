"""Product catalogue."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price_cents: int


def by_sku(products: list[Product]) -> dict[str, Product]:
    return {p.sku: p for p in products}
