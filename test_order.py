import unittest 
from order import Order
from drink import Drink

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.drink1 = Drink(base='sprite', price=3.50, size='small')
        self.drink2 = Drink(base='water', price=5.50, size='mega')
    
    def test_get_items(self):
        self.order.add_item(self.drink1)
        items = self.order.get_items()
        self.assertTrue(self.drink1 in items)
        
    def test_add_item(self):
        self.order.add_item(self.drink1)
        self.assertIn(self.drink1, self.order.get_items())

    def test_get_totals(self):
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        expected_total = self.drink1.get_total() + self.drink2.get_total()
        self.assertEqual(self.order.get_total(), expected_total)
        expected_total_with_tax = expected_total+ (expected_total * Order.tax_rate)
        self.assertEqual(self.order.get_total_with_tax(), expected_total_with_tax)

    def test_get_num_items(self):
        self.order.add_item(self.drink1)
        self.assertEqual(self.order.get_num_items(), "Item Total: 1")

    def test_get_receipt(self):
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        total = self.order.get_total()
        total_with_tax = self.order.get_total_with_tax()
        tax = total_with_tax - total
        expected_receipt = {
            'items': f"{self.drink1}, {self.drink2}",
            'total_before_tax': f"${total:.2f}",
            'tax': f"${tax:.2f}",
            'total_with_tax': f"{total_with_tax:.2f}"
        }
        
if __name__ == '__main__':
    unittest.main()