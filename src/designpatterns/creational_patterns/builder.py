from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import cappuccino_receipt, espresso_receipt, latte_receipt
from designpatterns.logger import logger


class CoffeeBuilder(ABC):
    """The Coffee interface specifies methods for selecting contents of coffee drink."""

    @property
    @abstractmethod
    def cup(self) -> None:
        """Set clean state (empty cup) for making coffee."""
        raise NotImplementedError

    @abstractmethod
    def select_coffee_amount(self) -> None:
        """Specify coffee amount to be used for coffee drink."""
        raise NotImplementedError

    def add_milk(self) -> None:
        """Specify milk amount to be used for coffee drink."""
        self._cup.add('No milk')

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for coffee drink."""
        self._cup.add('No milk foam')

    def add_chocolate(self) -> None:
        """Specify chocolate amount to be used for coffee drink."""
        self._cup.add('No chocolate')


class LatteBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Latte coffee drink."""

    def __init__(self) -> None:
        self.reset()

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
        self._cup.add(latte_receipt.coffee)

    def add_milk(self) -> None:
        """Specify milk amount to be used for latte coffee drink."""
        self._cup.add(latte_receipt.milk)

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for latte coffee drink."""
        self._cup.add(latte_receipt.milk_foam)


class Latte:
    """Get final latte coffee drink."""

    def __init__(self) -> None:
        self.contents = []

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final latte coffee drink contents."""
        logger.info(f"Your latte is made of {', '.join(self.contents)}.")


class CappuccinoBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Cappuccino coffee drink."""

    def __init__(self) -> None:
        self.reset()

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
        self._cup.add(cappuccino_receipt.coffee)

    def add_milk(self) -> None:
        """Specify milk amount to be used for cappuccino coffee drink."""
        self._cup.add(cappuccino_receipt.milk)

    def add_chocolate(self) -> None:
        """Specify chocolate to be used for cappuccino coffee drink."""
        self._cup.add(cappuccino_receipt.chocolate)

    def add_milk_foam(self) -> None:
        """Specify milk foam amount to be used for cappuccino coffee drink."""
        self._cup.add(cappuccino_receipt.milk_foam)


class Cappuccino:
    """Get final cappuccino coffee drink."""

    def __init__(self) -> None:
        self.contents = []

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final cappuccino coffee drink contents."""
        logger.info(f"Your cappuccino is made of {', '.join(self.contents)}.")


class EspressoBuilder(CoffeeBuilder):
    """Provides specific implementations of the building steps of Espresso coffee drink."""

    def __init__(self) -> None:
        self.reset()

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
        self._cup.add(espresso_receipt.coffee)


class Espresso:
    """Get final espresso coffee drink."""

    def __init__(self) -> None:
        self.contents = []

    def add(self, part: str) -> None:
        """Add coffee content."""
        self.contents.append(part)

    def list_contents(self) -> None:
        """List final espresso coffee drink contents."""
        logger.info(f"Your espresso is made of {', '.join(self.contents)}.")


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
