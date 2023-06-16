import json
from src import Item

FILEPATH = "test_data/menu_items.json"

with open(FILEPATH, "r") as f:
    TEST_DATA = json.load(f)


def test_init():
    item = Item("Pizza", 5.99, True)
    assert item.name == "Pizza"
    assert item.price == 5.99
    assert item.is_available() == True


def test_init_with_dict():
    item_dict = TEST_DATA[0]

    # Ensure the object we receive from indexing TEST_DATA is a dict.
    assert isinstance(item_dict, dict)

    item = Item.from_dict(item_dict)
    assert item.name == item_dict.get("name")
    assert item.price == item_dict.get("price")
    assert item.is_available() == item_dict.get("available")


def test_make_unavailable():
    item = Item("Chips", 2.40, True)
    item.make_unavailable()

    assert item.is_available() is False


def test_make_available():
    item = Item("Chips", 2.40, False)

    item.make_available()

    assert item.is_available() is True




