import pytest

from src.LawnGrass import LawnGrass


def test_lawngrass_init(lawngrass_1: LawnGrass) -> None:
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"
    assert lawngrass_1.quantity == 20


def test_smartphone_add(lawngrass_1: LawnGrass, lawngrass_2: LawnGrass) -> None:
    assert lawngrass_1 + lawngrass_2 == 16750.0


def test_smartphone_add_error(lawngrass_1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        lawngrass_1 + 1
