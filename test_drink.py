import unittest 
from drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink(base='sprite', price=3.50, size='small')
        
    def test_add_and_get_flavors(self): 
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_flavors(), ['strawberry'])

    def test__get_num_flavors(self):
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_num_flavors(), 1)

    def test_get_base(self):
        self.assertEqual(self.drink.get_base(), 'sprite')

    def test_get_total(self):
        self.assertEqual(self.drink.get_total(), 1.50)
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_total(), 1.65)

    def test_set_and_get_size(self):
        self.drink.set_size('mega')
        self.assertEqual(self.drink.get_total(), 2.50)

if __name__ == '__main__':
    unittest.main()
