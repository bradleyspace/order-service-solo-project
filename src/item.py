class Item:
    """
    Instance variables
    name: A string representing the dish name
    price: A float representing the price of the item
    available: A boolean representing whether the item is available or not
    """

    def __init__(self, name: str, price: float, available: bool) -> None:
        self.name = name
        self.price = price
        self.available = available

    @classmethod
    def from_dict(cls, _dict: dict):
        # Construct an Item from a dict
        return cls(
            _dict["name"],
            _dict["price"],
            _dict["available"]
        )

    def is_available(self) -> bool:
        return self.available

    def make_available(self):
        """
        Make an item available to order
        """
        self.available = True

    def make_unavailable(self):
        """
        Make an item unavailable to order.
        """
        self.available = False
