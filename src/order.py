from datetime import datetime
from .receipt import Receipt

class Order:
    """
    Instance variables:
    items: A list containing the items the customer has added to the order.
    completed: A boolean representing if the customer has checked out or not.
    """

    def __init__(self) -> None:
        pass

    def add_item(self, item) -> None:
        pass

    def remove_item(self, item) -> None:
        pass

    def checkout(self) -> Receipt:
        #
        pass

    def _get_estimated_arrival_time(self) -> datetime:
        pass

    def _send_order_sms_confirmation(self):
        pass