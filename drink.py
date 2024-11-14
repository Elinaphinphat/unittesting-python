class Drink:
    valid_bases = ['water', 'sprite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
# List of bases and flavors for the drinks.

    def __init__(self, base, price): # This is the constructor for the Drink class.
        if base not in Drink.valid_bases:
            raise ValueError("Invalid.")
        self.__base = base # Sets the drink base.
        self.__flavors = [] # Creates an empty list for flavors, hence the empty brackets '[]'.
        self.price = price # Sets the price for drinks.

    def get_flavors(self):
        return self.__flavors
    # Returns get_flavors, or the list of flavors.

    def get_base(self):
        return self.__base
    # Returns the drink base.

    def get_num_flavors(self):
        return len(self.__flavors)
    # Returns the number of flavors in the drink.

    def set_flavors(self, flavors): 
        if any(flavor not in Drink.valid_flavors for flavor in flavors):
            raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")
        self.__flavors = list(set(flavors))
    # This whole method will set the flavors for the drinks, and will raise a Value error if invalid.

    def add_flavors(self, flavor):
        if flavor not in Drink.valid_flavors:
            raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")
        if flavor not in self.__flavors:
            self.__flavors.append(flavor)
    # This whole method will add flavors to the drinks instead, and will raise a Value error if invalid.


    def __str__(self):
        return f'Drink base: {self.__base}, Drink flavor: {self.__flavors}, Drink price: ${self.price:.2f})'
    # This command will return the base, flavors, and the price of the drink as a string.
