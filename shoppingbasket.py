from dataclasses import dataclass
from typing import List
from item import Item
from functools import reduce

@dataclass
class Basket(object):
    items: List[Item]

    def total(self):
        return reduce(lambda subtotal, item: subtotal + (item.unit_price * item.quantity), self.items, 0)