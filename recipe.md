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
    
# File: src/menu.py
class Menu:
    """
    Instance variables
    items: A list of Item, representing all the items in the menu.
    """
    
    def __init__(self) -> None:
        """This function will open test_data/menu_items.json and add the items from there."""
        pass
    
    def add_new_item(self, item) -> None:
        """Add a new item to the list"""
        pass
    
    def get_all_items(self) -> list[Item]:
        """Return a list of all the items"""
        pass
    
    def get_available_items(self) -> list[Item]:
        """Returns a list of items that are marked as availale"""
        pass
    
    def get_unavailable_items(self) -> list[Item]:
        """Return a list of items that are marked as not available"""
        pass
    
    def get_by_name(self, name) -> Item:
        """Get a item by its name"""
        pass
        
    def create_order(self, item) -> Order:
        """
        Create a new order.
        Simply to prevent instantiating classes, you can have one entry file.
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
        """Add an item to your order"""
        pass
    
    def remove_item(self, item) -> None:
        """Remove an item from your order"""
        pass
    
    def checkout(self, phone_number: str) -> Receipt:
        """Finalize the order, generate a receipt and send a SMS to your  phone"""
        pass

    def get_estimated_arrival_time(self) -> datetime:
        pass

    def _send_order_sms_confirmation(self):
        pass
```

### Examples

```py
menu = Menu() # Create a menu instance
order = menu.create_order() # Start a new order (Returns a instance of Order)
item = menu.get_by_name("Pizza") # Get an item
order.add(item) # Add the item to the order
receipt = order.checkout("+44 1234 567890") # Checkout with your phone number and get the receipt.

print(receipt.total_price)
```
```py
# Alternatively you can construct an order without using Menu.create_order
menu = Menu()
order = Order()
item_1 = menu.get_by_name("Pizza")
item_2 = menu.get_by_name("Chips")
order.add(item_1)
order.add(item_2)

receipt = order.checkout("+44 09876 54321")
print(receipt.total_price)
```