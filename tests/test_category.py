import pytest

from src.Category import Category
from src.Products import Product


def test_categories(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получение дополнительных функций для удобства жизни")
    assert Category.product_count == 2
    assert Category.category_count == 1


def test_products_add(category: Category, prod_3: Product) -> None:
    Category.product_count = 2
    Category.category_count = 1
    category.add_product(prod_3)
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получение дополнительных функций для удобства жизни")
    assert Category.product_count == 3
    assert Category.category_count == 1
    assert category.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. "
                                 "Остаток: 8 шт.\nIphone 16, 250000.0 руб. Остаток: 2 шт.\n")


def test_str_category(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 13 шт.\n"


def test_products_add_error(category: Category) -> None:
    with pytest.raises(TypeError):
        category.add_product("No product")


def test_middle_price(category: Category) -> None:
    assert category.middle_price() == 195000.0


def test_middle_price_empty(category_2: Category) -> None:
    assert category_2.middle_price() == 0
