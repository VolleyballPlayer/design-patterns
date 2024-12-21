import pytest

from designpatterns.creational_patterns.builder import (
    Cappuccino,
    CappuccinoBuilder,
    CoffeeBuilder,
    Director,
    Espresso,
    EspressoBuilder,
    Latte,
    LatteBuilder,
)
from designpatterns.helpers.receipts import cappuccino_receipt, espresso_receipt, latte_receipt


class TestBuilder:
    class TestCoffeeBuilder(CoffeeBuilder):
        def __init__(self) -> None:
            self.reset()

        def reset(self) -> None:
            self._cup = Latte()

        @property
        def cup(self) -> None:
            cup = self._cup
            self.reset()
            return cup

        def select_coffee_amount(self) -> None:
            raise NotImplementedError()

    def test__latte_preparation__all_ingredients_used(self, caplog: pytest.LogCaptureFixture) -> None:
        director = Director()

        builder = LatteBuilder()
        director.builder = builder
        director.build_latte()
        builder.cup.list_contents()

        assert 'Your latte is made of 1/2 cup coffee, 1/4 cup milk, 1/4 cup milk foam.' in caplog.text

    def test__cappuccino_preparation__all_ingredients_used(self, caplog: pytest.LogCaptureFixture) -> None:
        director = Director()

        builder = CappuccinoBuilder()
        director.builder = builder
        director.build_cappuccino()
        builder.cup.list_contents()

        assert (
            'Your cappuccino is made of 1/2 cup coffee, 1/6 cup milk, 1/6 cup chocolate, 1/6 cup milk foam.'
            in caplog.text
        )

    def test__espresso_preparation__all_ingredients_used(self, caplog: pytest.LogCaptureFixture) -> None:
        director = Director()

        builder = EspressoBuilder()
        director.builder = builder
        director.build_espresso()
        builder.cup.list_contents()

        assert 'Your espresso is made of 1 shot coffee.' in caplog.text

    def test__latte_builder_add_milk__no_milk(self) -> None:
        builder = TestBuilder.TestCoffeeBuilder()
        builder.add_milk()
        assert builder.cup.contents == [None]

    def test__latte_builder_add_milk_foam__no_milk_foam(self) -> None:
        builder = TestBuilder.TestCoffeeBuilder()
        builder.add_milk_foam()
        assert builder.cup.contents == [None]

    def test__latte_builder_add_chocolate__no_chocolate(self) -> None:
        builder = TestBuilder.TestCoffeeBuilder()
        builder.add_chocolate()
        assert builder.cup.contents == [None]

    def test__latte_builder__set_receipt(self) -> None:
        builder = LatteBuilder()
        builder.receipt = latte_receipt
        assert builder.receipt.name == "latte"

    def test__latte__set_receipt(self) -> None:
        builder = Latte()
        builder.receipt = latte_receipt
        assert builder.receipt.name == "latte"

    def test__cappuccino__set_receipt(self) -> None:
        builder = Cappuccino()
        builder.receipt = cappuccino_receipt
        assert builder.receipt.name == "cappuccino"
    
    def test__espresso__set_receipt(self) -> None:
        builder = Espresso()
        builder.receipt = espresso_receipt
        assert builder.receipt.name == "espresso"
