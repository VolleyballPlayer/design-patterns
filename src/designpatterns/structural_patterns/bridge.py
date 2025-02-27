from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt
from designpatterns.logger import logger


class Abstraction:
    """The Abstraction defines the interface for the "control" part of the two class hierarchies.

    It maintains a reference to an object of the Implementation hierarchy and delegates all of the real work to this
    object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def prepare(self) -> str:
        """Prepare coffee drink."""
        logger.info('Abstraction: Base operation with:')
        self.implementation.prepare()


class Coffee(Abstraction):
    """You can extend the Abstraction without changing the Implementation classes."""

    def prepare(self) -> str:
        """Prepare coffee drink."""
        logger.info('ExtendedAbstraction: Extended operation with:')
        self.implementation.prepare()


class Implementation(ABC):
    """The Implementation defines the interface for all implementation classes.

    It doesn't have to match the Abstraction's interface. In fact, the two interfaces can be entirely different.
    Typically the Implementation interface provides only primitive operations, while the Abstraction defines
    higher-level operations based on those primitives.
    """

    @abstractmethod
    def prepare(self) -> str:
        """Prepare coffee drink."""


"""
Each Concrete Implementation corresponds to a specific platform and implements the Implementation interface using that
platform's API.
"""


class Latte(Implementation):
    """Implement latte preparation."""

    def prepare(self) -> str:
        """Prepare coffee drink."""
        Receipt.get_coffee(receipt=latte_receipt)


class Cappuccino(Implementation):
    """Implement cappuccino preparation."""

    def prepare(self) -> str:
        """Prepare coffee drink."""
        Receipt.get_coffee(receipt=cappuccino_receipt)


def client_code(abstraction: Abstraction) -> None:
    """Implement client code.

    Except for the initialization phase, where an Abstraction object gets linked with a specific Implementation object,
    the client code should only depend on the Abstraction class.
    This way the client code can support any abstraction-implementation combination.
    """
    abstraction.prepare()
