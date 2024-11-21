from drink import Drink
from order import Order

drink1 = Drink(base='sprite', price=3.50, size='small') 
drink1.add_flavors('lemon')

drink2 = Drink(base='water', price=6.50, size='large')
drink2.add_flavors('cherry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')

order = Order()
order.add_item(drink1)
order.add_item(drink2)

print("Item Order:")
for item in order.get_items():
    print(item)

print("\nTotal Items:", order.get_num_items())

receipt = order.get_receipt()
print("\nReceipt:")
print(f"Items:\n{receipt['items']}")
print(f"Number of Items: {receipt['num_items']}")
print(f"Total Before Tax: {receipt['total_before_tax']}")
print(f"Tax: {receipt['tax']}")
print(f"Total With Tax: {receipt['total_with_tax']}")