import json
import pytest
from src import Menu, Order
from src.exceptions import DuplicateItemError
from unittest.mock import Mock

FILEPATH = "test_data/menu_items.json"

with open(FILEPATH, "r") as f:
    TEST_DATA = json.load(f)


def test_menu_init():
    menu = Menu()
    assert len(menu.get_all_items()) == len(TEST_DATA)


def test_add_item():
    menu = Menu()
    fake_item = Mock()

    menu.add_new_item(fake_item)

    assert fake_item in menu.get_all_items()


def test_add_duplicate_item():
    menu = Menu()
    fake_item = Mock()

    menu.add_new_item(fake_item)

    with pytest.raises(DuplicateItemError) as e:
        menu.add_new_item(fake_item)

    assert str(e.value) == "Duplicate item added"

def test_get_available_items():
    menu = Menu()

    available_data = list(filter(lambda e: e["available"], TEST_DATA))
    available_items = menu.get_available_items()

    obj_names = [item.name for item in available_items]
    data_names = [item["name"] for item in available_data]

    # They had to be converted to the item names since the comparison would be between a dict and Item object
    assert all(name in obj_names for name in data_names)


def test_get_unavailable_items():
    menu = Menu()

    unavailable_data = list(filter(lambda e: not e["available"], TEST_DATA))
    unavailable_items = menu.get_unavailable_items()

    obj_names = [item.name for item in unavailable_items]
    data_names = [item["name"] for item in unavailable_data]

    # They had to be converted to the item names since the comparison would be between a dict and Item object
    assert all(name in obj_names for name in data_names)

def test_get_by_name():
    menu = Menu()

    first_object = TEST_DATA[0]
    data_name = first_object["name"]

    item = menu.get_by_name(data_name)

    assert item.name == data_name and item.price == first_object["price"]


def test_create_order():
    menu = Menu()
    order = menu.create_order()
    assert isinstance(order, Order)
