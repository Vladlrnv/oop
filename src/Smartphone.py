from typing import Any

from src.Products import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Any:
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError
