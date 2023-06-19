import pytest
from unittest.mock import Mock
from src import Order, Receipt
from datetime import datetime, timedelta


def test_initially_empty_and_incomplete():
    order = Order()

    assert len(order.items) == 0
    assert order.completed is False


def test_add_item():
    order = Order()
    fake_item = Mock()

    order.add_item(fake_item)

    assert fake_item in order.items


def test_remove_item():
    order = Order()
    fake_item = Mock()

    order.add_item(fake_item)
    order.remove_item(fake_item)

    assert fake_item not in order.items


def test_checkout():
    fake_item_1 = Mock()
    fake_item_2 = Mock()
    fake_item_1.name = "Pizza"
    fake_item_2.name = "Chips"
    fake_item_1.price = 9.99
    fake_item_2.price = 2.99

    order = Order()

    order.add_item(fake_item_1)
    order.add_item(fake_item_2)

    receipt = order.checkout(False)

    assert isinstance(receipt, Receipt)


def test_checkout_with_no_items():
    order = Order()

    with pytest.raises(Exception) as e:
        order.checkout()

    assert str(e.value) == "Attempted checkout with 0 items."


def test_get_estimated_arrival_time():
    fake_item_1 = Mock()
    fake_item_1.name = "Pizza"
    fake_item_1.price = 9.99

    order = Order()
    order.add_item(fake_item_1)

    order.checkout(False)

    estimated_time = order._get_estimated_arrival_time()
    diff = int((estimated_time - datetime.now()).total_seconds() / 60)

    assert round(diff, -1) == 30




