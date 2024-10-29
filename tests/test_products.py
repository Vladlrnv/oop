import pytest

from src.Products import Product


def test_product(prod_1: Product, prod_2: Product) -> None:
    assert prod_1.name == "Samsung Galaxy C23 Ultra"
    assert prod_1.description == "256GB, Серый цвет, 200MP камера"
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5
    assert prod_2.name == "Iphone 15"
    assert prod_2.description == "512GB, Gray space"
    assert prod_2.price == 210000.0
    assert prod_2.quantity == 8


def test_new_product(new_product: Product) -> None:
    assert new_product.name == "Samsung Galaxy S24 Ultra"
    assert new_product.description == "516GB, Белый цвет, 250MP камера"
    assert new_product.price == 200000.0
    assert new_product.quantity == 4


def test_price(prod_1: Product) -> None:
    prod_1.price = 100000
    assert prod_1.price == 100000
    prod_1.price = 0
    assert prod_1.price == 100000
    prod_1.price = -100
    assert prod_1.price == 100000


def test_str(prod_1: Product) -> None:
    assert str(prod_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток 5 шт.\n"


def test_add(prod_1: Product, prod_2: Product) -> None:
    assert prod_1 + prod_2 == 2580000


def test_add_error(prod_1: Product) -> None:
    with pytest.raises(TypeError):
        prod_1 + 1


def test_invalid_prod() -> None:
    with pytest.raises(ValueError) as e_info:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


