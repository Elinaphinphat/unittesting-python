from drink import Drink
from order import Order
# these two commands will import the classes for order.py and drink.py

drink1 = Drink(base='sprite', price=3.50) 
drink1.add_flavors('lemon')
# An example order that test whether the inner API is working properly or not.

drink2 = Drink(base='water', price=6.50)
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

print(order.get_items())
print(order.get_num_items())
print(order.get_receipt())
# This will print the receipt and items into the console.