# Recipe

### Requirements:

- [ ] See a menu, with the prices
- [ ] Create an order that has multiple items the customer selects
- [ ] Generate an itemised receipt with the total
- [ ] Send an SMS order containing the order confirmation and the estimated time of arrival

### Class Design

```py
from datetime import datetime

# File: src/receipt.py
class Receipt:
    """
    Instance variables
    items: A list of Item, representing the items purchased
    total_price: A float representing the cost of the order
    """
    
    def __init__(self, items, total_price) -> None:
        pass
    
# File: src/item.py
class Item:
    """
    Instance variables
    name: A string representing the dish name
    price: A float representing the price of the item
    available: A boolean representing whether the item is available or not
    """
    
    def __init__(self, item, price, available) -> None:
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
    
# File: src/menu.py
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

# File: src/order.py
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

    def get_estimated_arrival_time(self) -> datetime:
        pass

    def _send_order_sms_confirmation(self):
        pass
```