# Recipe

### Requirements:

- [ ] See a menu, with the prices
- [ ] Create an order that has multiple items the customer selects
- [ ] Generate an itemised receipt with the total
- [ ] Send an SMS order containing the order confirmation and the estimated time of arrival

### Class Design

```py
from datetime import datetime

# File: src/exceptions.py

class DuplicateItemError(Exception):
    
    def __init__(self, message="Duplicate item added"):
        super().__init__(message)

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

### Tests

#### Item Tests

```py
# File: tests/test_item.py

# Test that the Item class is constructed properly
item = Item("Pizza", 1.00, True)
assert item.name == "Pizza"
assert item.price == 1.00
assert item.is_available() is True

# Test that the Item.from_dict constructs properly

item = Item.from_dict({"name": "Pizza", "price": 1.00, "available": True})
assert item.name == "Pizza"
assert item.price == 1.00
assert item.is_available() is True

# Test that make_available and make_unavailable works as intended

item = Item("Pizza", 1.00, True)

item.make_unavailable()
assert item.is_available() is False

item.make_available()
assert item.is_available() is True
```

#### Menu Tests

```py
# File: tests/test_menu.py

# Test that the Menu task constructs properly and loads the data
# from menu_items.json
menu = Menu()
file = open("test_data.json")
data = json.load(file)
file.close()

assert len(menu.get_all_items()) == len(data)

# Test the add_new_item method

menu = Menu()
item = Item("Curry", 4.00, True)
menu.add_new_item(item)

assert item in menu.get_all_items()

# Test adding a duplicate item

menu = Menu()
item = Item("Kebab", 5.00, True)

menu.add_new_item(item)

with pytest.raises(DuplicateItemError) as e:
    menu.add_new_item(item)

assert str(e.value) == "Duplicate item added"

# Test get_available_items

menu = Menu()
file = open("test_data.json")
data = json.load(file)
file.close()

data_available = list(filter(lambda e: e["available"], data))
menu_available_items = menu.get_available_items()

assert all(item in menu_available_items for item in data_available)

# Test get_unavailable_items
menu = Menu()
file = open("test_data.json")
data = json.load(file)
file.close()

data_unavailable = list(filter(lambda e: not e["available"], data))
menu_unavailable_items = menu.get_unavailable_items()

assert all(item in menu_unavailable_items for item in data_unavailable)

# Test get by name

menu = Menu()
item = Item("Kebab", 5.00, True)
menu.add_new_item(item)

result = menu.get_by_name("kebab")

assert result == item

# Test create order:

menu = Menu()
order = menu.create_order()

assert isinstance(order, Order)
```

### Order Tests

```py 

# Test initially empty and incomplete
order = Order()
assert len(order.items) == 0
assert not order.completed

# Test add item

item = Mock()
order = Order()
order.add_item(item)
assert item in order.items

# Test remove item

item = Mock()
order = Order()
order.add_item(item)

order.remove_item(item)
assert item not in order.items

# Test Checkout

fake_item_1 = Mock()
fake_item_2 = Mock()
fake_item_1.name = "Pizza"
fake_item_2.name = "Chips"
fake_item_1.price = 9.99
fake_item_2.price = 2.99

order = Order()

order.add_item(fake_item_1)
order.add_item(fake_item_2)

receipt = order.checkout()

assert isinstance(receipt, Receipt)
```