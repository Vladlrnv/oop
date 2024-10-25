from typing import Any

from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """ Класс, определяющий вид товара """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """ Функция инициализации """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product: dict) -> Any:
        """ Метод, позволяющий добавить новый продукт в виде словаря"""
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self) -> Any:
        """ Декоратор для чтения приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, new_value: int) -> Any:
        """ Сеттер для присвоения атрибуту __price нового значения """
        if new_value > 0:
            self.__price = new_value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> Any:
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт.\n"

    def __add__(self, other: Any) -> Any:
        if type(other) is Product:
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            raise TypeError
