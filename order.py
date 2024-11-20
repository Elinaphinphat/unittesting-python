class Order:
    tax_rate = 0.0725

    def __init__(self):
        self.__items = [] 
# __init__ is used as a constructor which creates an empty order object.

# -------------
    def get_items(self):
        return self.__items # This will return the list of drinks in the order.
    
    def add_item(self, drink):
        self.__items.append(drink) # This is used to add drinks into the Order.
# -------------

    def get_total(self):
        total = sum(drink.get_total for drink in self.__items)
        return total
    # This will calculate and sum up the drink prices

    def get_total_with_tax(self):
        total = self.get_total()
        tax = total * self.tax_rate
        return total + tax

    def get_num_items(self):
        num_items = len(self.__items)
        return f"Item Total: {num_items}"
    # This will return the total number of drinks in the receipt.

    def get_total(self):
        return sum(drink.get_total() for drink in self.__items)

    def get_receipt(self):
        receipt = "\n".join([str(item) for item in self.__items])
        total = self.get_total()
        total_with_tax = self.get_total_with_tax()
        tax = total_with_tax - total
        return {
            'items': receipt,
            'num_items': len(self.__items),
            'total_before_tax': f"${total:.2f}",
            'tax': f"${(total_with_tax - total):.2f}",
            'total_with_tax': f"S{total_with_tax:.2f}"
        }
    
    # Returns a receipt in a specific formatted order into the console.

    def remove_item(Self, index):
        if 0 <= index < len(self.__items):
            self.__items.pop(index)
        else:
            raise IndexError("Invalid, can't be removed.")
    # Removes items from the order using index.

    def __str__(self):
        return f'Order(items={self.__items})'
    # Returns a list of all items.