class Item:
    """
    Instance variables
    name: A string representing the dish name
    price: A float representing the price of the item
    available: A boolean representing whether the item is available or not
    """

    def __init__(self, name: str, price: float, available: bool) -> None:
        pass

    @classmethod
    def from_dict(cls, _dict: dict):
        # Construct an Item from a dict
        pass

    def make_available(self):
        """
        Make an item available to order
        """
        pass

    def make_unavailable(self):
        """
        Make an item unavailable to order.
        """
        pass