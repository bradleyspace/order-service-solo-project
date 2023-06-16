import json
from .item import Item
from .order import Order
from .exceptions import DuplicateItemError


class Menu:
    """
    Instance variables
    items: A list of Item, representing all the items in the menu.
    """

    def __init__(self) -> None:
        self.items = []
        self._load_data()

    def _load_data(self):
        with open("test_data/menu_items.json") as f:
            data = json.load(f)
            for item in data:
                self.items.append(Item.from_dict(item))

    def add_new_item(self, item) -> None:
        if item in self.items:
            raise DuplicateItemError()
        self.items.append(item)

    def get_all_items(self) -> list[Item]:
        return self.items

    def get_available_items(self) -> list[Item]:
        return list(filter(lambda e: e.available, self.items))

    def get_unavailable_items(self) -> list[Item]:
        return list(filter(lambda e: e.available, self.items))

    def get_by_name(self, name) -> Item:
        return list(filter(lambda e: e.name == name, self.items))[0] or None

    def create_order(self) -> Order:
        """
        Create a new order.
        Simply to prevent instantiating classes, you can have one entry point.
        """
        return