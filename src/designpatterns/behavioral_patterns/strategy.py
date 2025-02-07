from __future__ import annotations

from abc import ABC, abstractmethod

from tabulate import tabulate

from designpatterns.helpers.receipts import (
    Receipt,
    cappuccino_receipt,
    espresso_receipt,
    latte_receipt,
)
from designpatterns.logger import logger


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
        logger.info('Preparing latte:')
        print(
            tabulate(
                [[latte_receipt.name, latte_receipt.coffee, latte_receipt.milk, latte_receipt.milk_foam]],
                tablefmt='psql',
            )
        )


class StrategyCappuccino(Strategy):
    """Get prepared cappuccino coffee drink."""

    def make_coffee(self) -> None:
        """Prepare cappuccino coffee drink."""
        logger.info(
            f'Your {cappuccino_receipt.name} will be prepared using following ingredients: \n\
{cappuccino_receipt.coffee}\n{cappuccino_receipt.milk}\n{cappuccino_receipt.milk_foam}\n{cappuccino_receipt.chocolate}'
        )


class StrategyEspresso(Strategy):
    """Get prepared espresso coffee drink."""

    def make_coffee(self) -> None:
        """Prepare espresso coffee drink."""
        Receipt.get_coffee(espresso_receipt)
