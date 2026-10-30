import pytest

from shop.pricing import apply_discount, order_total


def test_discount_rounds_down():
    assert apply_discount(999, 10) == 899


def test_discount_rejects_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_order_total_adds_shipping():
    assert order_total([100, 250], shipping_cents=50) == 400
