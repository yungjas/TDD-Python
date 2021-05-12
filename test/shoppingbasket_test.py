# in tdd, tests drive the design of our code
# fail test cases first
# pass
# reiterate: refactor code

import unittest
from shoppingbasket import Basket
from item import Item
from dataclasses import dataclass

class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        # generates a constructor
        basket = Basket([])
        # amount in basket should be equals to 0
        self.assertEqual(basket.total(), 0)
    
    def test_single_item_quantity_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)
    
    def test_two_items_quantity_two(self):
        basket = Basket([Item(100.0, 2)])
        self.assertEqual(basket.total(), 200.0)
    
    def test_two_items_quantity_single(self): # 2 items with 1 quantity
        basket = Basket([Item(100.0, 1), Item(100.0, 1)])
        self.assertEqual(basket.total(), 200.0)

if __name__ == "main":
    pass