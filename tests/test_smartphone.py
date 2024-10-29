import pytest

from src.Smartphone import Smartphone


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.memory == 256
    assert smartphone.model == "S23 Ultra"
    assert smartphone.color == "Серый"
    assert smartphone.efficiency == 95.5
    assert smartphone.quantity == 5


def test_smartphone_add(smartphone: Smartphone, smartphone2: Smartphone) -> None:
    assert smartphone + smartphone2 == 2580000.0


def test_smartphone_add_error(smartphone: Smartphone) -> None:
    with pytest.raises(TypeError):
        smartphone + 1
