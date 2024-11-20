from drink import Drink
from order import Order
# these two commands will import the classes for order.py and drink.py

drink1 = Drink(base='sprite', price=3.50, size='small') 
drink1.add_flavors('lemon')
# An example order that test whether the inner API is working properly or not.

drink2 = Drink(base='water', price=6.50, size='large')
drink2.add_flavors('cherry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
# An example order that test whether the inner API is working properly or not.

order = Order()
order.add_item(drink1)
order.add_item(drink2)
# Adds the orders into the receipt.

def get_receipt_data(order):
    return order.get_receipt()

receipt_data = get_receipt_data(order)
receipt_data
# Gives raw data through API