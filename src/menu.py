class Menu:
    """
    Instance variables
    items: A list of Item, representing all the items in the menu.
    """

    def __init__(self) -> None:
        pass

    def add_new_item(self, item) -> None:
        pass

    def get_all_items(self) -> list[Item]:
        pass

    def get_available_items(self) -> list[Item]:
        pass

    def get_unavailable_items(self) -> list[Item]:
        pass

    def get_by_name(self, name) -> Item:
        pass

    def create_order(self, item) -> Order:
        """
        Create a new order.
        Simply to prevent instantiating classes, you can have one entry point.
        """
        pass