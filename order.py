class Order:
    tax_rate = 0.0725

    def __init__(self):
        self.__items = [] 

    def get_items(self):
        return self.__items 
    
    def add_item(self, drink):
        self.__items.append(drink) 

    def get_total(self):
        total = sum(drink.get_total for drink in self.__items)
        return total

    def get_total_with_tax(self):
        total = self.get_total()
        tax = total * self.tax_rate
        return total + tax

    def get_num_items(self):
        num_items = len(self.__items)
        return f"Item Total: {num_items}"

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

    def remove_item(Self, index):
        if 0 <= index < len(self.__items):
            self.__items.pop(index)
        else:
            raise IndexError("Invalid, can't be removed.")

    def __str__(self):
        return f'Order(items={self.__items})'
