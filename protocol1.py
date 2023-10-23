from typing import List


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Product]) -> float:
    return sum([item.quantity * item.price for item in items])