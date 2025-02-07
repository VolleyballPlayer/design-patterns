from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import (
    Receipt,
    cappuccino_receipt,
    double_espresso_receipt,
    espresso_receipt,
    latte_receipt,
    triple_espresso_receipt,
)


class Context:
    """The Context defines the interface of interest to clients."""

    def __init__(self, strategy: Strategy) -> None:
        """Usually, the Context accepts a strategy through the constructor.

        But also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """The Context maintains a reference to one of the Strategy objects.

        The Context does not know the concrete class of a strategy.
        It should work with all strategies via the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Usually, the Context allows replacing a Strategy object at runtime."""
        self._strategy = strategy

    def prepare_coffee(self) -> None:
        """Delegate some work to the Strategy object.

        It does not implement multiple versions of the algorithm on its own.
        """
        self._strategy.make_coffee()


class Strategy(ABC):
    """The Strategy interface declares operations common to all supported versions of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def make_coffee(self) -> None:
        """Get coffee receipt and prepare coffee."""


class StrategyLatte(Strategy):
    """Get prepared latte coffee drink."""

    def make_coffee(self) -> None:
        """Prepare latte coffee drink."""
        Receipt.get_coffee(latte_receipt)


class StrategyCappuccino(Strategy):
    """Get prepared cappuccino coffee drink."""

    def make_coffee(self) -> None:
        """Prepare cappuccino coffee drink."""
        Receipt.get_coffee(cappuccino_receipt)


class StrategyEspresso(Strategy):
    """Get prepared espresso coffee drink."""

    def make_coffee(self) -> None:
        """Prepare espresso coffee drink."""
        Receipt.get_coffee(espresso_receipt)


class StrategyDoubleEspresso(Strategy):
    """Get prepared double espresso coffee drink."""

    def make_coffee(self) -> None:
        """Prepare double espresso coffee drink."""
        Receipt.get_coffee(double_espresso_receipt)


class StrategyTripleEspresso(Strategy):
    """Get prepared triple espresso coffee drink."""

    def make_coffee(self) -> None:
        """Prepare triple espresso coffee drink."""
        Receipt.get_coffee(triple_espresso_receipt)
