from dataclasses import dataclass
from typing import List

@dataclass
class Item(object):
    unit_price: float
    quantity: int