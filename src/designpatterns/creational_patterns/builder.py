from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.creational_patterns.singleton import CountCoffeeSingleton
from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, espresso_receipt, latte_receipt


class CoffeeBuilder(ABC):
    """The Coffee interface specifies methods for selecting contents of coffee drink."""

    @property
    @abstractmethod
    def cup(self) -> None:
        """Set clean state (empty cup) for making coffee."""

    @property
    def receipt(self) -> Receipt:
        """Get receipt attribute."""
        return self._receipt

    @receipt.setter
    def receipt(self, new_receipt: Receipt) -> Receipt:
        """Set receipt attribute."""
        self._receipt = new_receipt

    @abstractmethod
    def select_coffee_amount(self) -> None:
        """Specify coffee amount to be used for coffee drink."""

    def add_milk(self) -> None:
        """Specify milk amount to be used for coffee drink."""
        self._cup.add(None)

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for coffee drink."""
        self._cup.add(None)

    def add_chocolate(self) -> None:
        """Specify chocolate amount to be used for coffee drink."""
        self._cup.add(None)


class LatteBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Latte coffee drink."""

    def __init__(self) -> None:
        self.reset()
        self._receipt = latte_receipt

    def reset(self) -> None:
        """Reset to blank latte coffee drink in fresh builder instance."""
        self._cup = Latte()

    @property
    def cup(self) -> Latte:
        """Reset to blank latte coffee drink after returning the end result to the client.

        This makes it possible to have the builder instance ready to start producing another cup.
        """
        cup = self._cup
        self.reset()
        return cup

    def select_coffee_amount(self) -> None:
        """Specify coffee amount to be used for latte coffee drink."""
        self._cup.add(self._receipt.coffee)

    def add_milk(self) -> None:
        """Specify milk amount to be used for latte coffee drink."""
        self._cup.add(self._receipt.milk)

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for latte coffee drink."""
        self._cup.add(self._receipt.milk_foam)


class Latte:
    """Get final latte coffee drink."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = latte_receipt

    @property
    def receipt(self) -> Receipt:
        """Get receipt attribute."""
        return self._receipt

    @receipt.setter
    def receipt(self, new_receipt: Receipt) -> Receipt:
        """Set receipt attribute."""
        self._receipt = new_receipt

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final latte coffee drink contents."""
        Receipt.get_coffee(receipt=self._receipt, ingredients=self.contents)


class CappuccinoBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Cappuccino coffee drink."""

    def __init__(self) -> None:
        self.reset()
        self._receipt = cappuccino_receipt

    def reset(self) -> None:
        """Reset to blank cappuccino coffee drink in fresh builder instance."""
        self._cup = Cappuccino()

    @property
    def cup(self) -> Cappuccino:
        """Reset to blank cappuccino coffee drink after returning the end result to the client.

        This makes it possible to have the builder instance ready to start producing another cup.
        """
        cup = self._cup
        self.reset()
        return cup

    def select_coffee_amount(self) -> None:
        """Specify coffee amount to be used for cappuccino coffee drink."""
        self._cup.add(self._receipt.coffee)

    def add_milk(self) -> None:
        """Specify milk amount to be used for cappuccino coffee drink."""
        self._cup.add(self._receipt.milk)

    def add_chocolate(self) -> None:
        """Specify chocolate to be used for cappuccino coffee drink."""
        self._cup.add(self._receipt.chocolate)

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for cappuccino coffee drink."""
        self._cup.add(self._receipt.milk_foam)


class Cappuccino:
    """Get final cappuccino coffee drink."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = cappuccino_receipt

    @property
    def receipt(self) -> Receipt:
        """Get receipt attribute."""
        return self._receipt

    @receipt.setter
    def receipt(self, new_receipt: Receipt) -> Receipt:
        """Set receipt attribute."""
        self._receipt = new_receipt

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final cappuccino coffee drink contents."""
        Receipt.get_coffee(receipt=self._receipt, ingredients=self.contents)


class EspressoBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Espresso coffee drink."""

    def __init__(self) -> None:
        self.reset()
        self._receipt = espresso_receipt

    def reset(self) -> None:
        """Reset to blank espresso coffee drink in fresh builder instance."""
        self._cup = Espresso()

    @property
    def cup(self) -> Espresso:
        """Reset to blank espresso coffee drink after returning the end result to the client.

        This makes it possible to have the builder instance ready to start producing another cup.
        """
        cup = self._cup
        self.reset()
        return cup

    def select_coffee_amount(self) -> None:
        """Specify coffee amount to be used for espresso coffee drink."""
        self._cup.add(self._receipt.coffee)


class Espresso:
    """Get final espresso coffee drink."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = espresso_receipt

    @property
    def receipt(self) -> Receipt:
        """Get receipt attribute."""
        return self._receipt

    @receipt.setter
    def receipt(self, new_receipt: Receipt) -> Receipt:
        """Set receipt attribute."""
        self._receipt = new_receipt

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final espresso coffee drink contents."""
        Receipt.get_coffee(receipt=self._receipt, ingredients=self.contents)


class Director:
    """Execute the building steps in a particular sequence according to standard coffee drinks mixtures."""

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> CoffeeBuilder:
        """Get to director any builder provided by client as director can work with any of them (and new ones)."""
        return self._builder

    @builder.setter
    def builder(self, builder: CoffeeBuilder) -> None:
        self._builder = builder
        CountCoffeeSingleton().count()

    def build_latte(self) -> None:
        """Construct latte."""
        self.builder.select_coffee_amount()
        self.builder.add_milk()
        self.builder.add_milk_foam()

    def build_cappuccino(self) -> None:
        """Construct cappuccino."""
        self.builder.select_coffee_amount()
        self.builder.add_milk()
        self.builder.add_chocolate()
        self.builder.add_milk_foam()

    def build_espresso(self) -> None:
        """Construct espresso."""
        self.builder.select_coffee_amount()
