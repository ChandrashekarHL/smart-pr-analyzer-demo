import pytest

from shop.pricing import apply_discount, order_total, split_evenly


def test_discount_rounds_down():
    assert apply_discount(999, 10) == 899


def test_discount_rejects_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_order_total_adds_shipping():
    assert order_total([100, 250], shipping_cents=50) == 400


def test_split_evenly_adds_up_and_differs_by_at_most_one():
    parts = split_evenly(1000, 3)
    assert parts == [334, 333, 333] and sum(parts) == 1000


def test_split_evenly_rejects_bad_input():
    with pytest.raises(ValueError):
        split_evenly(100, 0)
    with pytest.raises(ValueError):
        split_evenly(-1, 2)
