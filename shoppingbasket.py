from dataclasses import dataclass
from typing import List
from item import Item
from functools import reduce

@dataclass
class Basket(object):
    items: List[Item]

    def total(self):
        # how reduce works:
        # At first step, first two elements of sequence are picked and the result is obtained.
        # Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
        # This process continues till no more elements are left in the container
        # from: https://www.geeksforgeeks.org/reduce-in-python/
        return reduce(lambda subtotal, item: subtotal + (item.unit_price * item.quantity), self.items, 0)