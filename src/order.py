from datetime import datetime, timedelta
from .receipt import Receipt

class Order:
    """
    Instance variables:
    items: A list containing the items the customer has added to the order.
    completed: A boolean representing if the customer has checked out or not.
    """

    def __init__(self) -> None:
        self.items = []
        self.completed = False

    def add_item(self, item) -> None:
        self.items.append(item)

    def remove_item(self, item) -> None:
        self.items.remove(item)

    def checkout(self, _send_sms=True) -> Receipt:
        if len(self.items) == 0:
            raise Exception("Attempted checkout with 0 items.")
        total_price = sum([item.price for item in self.items])
        return Receipt(self.items, total_price)

    def _get_estimated_arrival_time(self) -> datetime:
        if self.completed:
            raise Exception("Order is not completed")

        return datetime.now() + timedelta(minutes=30)

    def _send_order_sms_confirmation(self):
        pass