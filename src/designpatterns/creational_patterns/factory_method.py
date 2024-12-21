from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, espresso_receipt, latte_receipt


class CoffeeCreator(ABC):
    """Declares the factory method (select_coffee) that is supposed to return an object of a Product class.

    The Creator's subclasses usually provide the implementation of this method.
    """

    @abstractmethod
    def select_coffee(self) -> Product:
        """May also provide some default implementation of the factory method."""

    def prepare(self) -> None:
        """Despite its name, the Creator's primary responsibility is not creating products.

        Usually, it contains some core business logic that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the factory method and returning a different
        type of product from it.
        """
        product = self.select_coffee().get_receipt()
        product.get_coffee()


class LatteCreator(CoffeeCreator):
    """The signature of the method still uses the abstract product type, even though the concrete product is returned.

    This way the Creator can stay independent of concrete product classes.
    """

    def select_coffee(self) -> Product:
        """Select latte coffee drink product."""
        return LatteProduct()


class CappuccinoCreator(CoffeeCreator):
    """Define cappuccino coffee drink creator."""

    def select_coffee(self) -> Product:
        """Select cappuccino coffee drink product."""
        return CappuccinoProduct()


class EspressoCreator(CoffeeCreator):
    """Define espresso coffee drink creator."""

    def select_coffee(self) -> Product:
        """Select espresso coffee drink product."""
        return EspressoProduct()


class Product(ABC):
    """The Product interface declares the operations that all concrete products must implement."""

    @abstractmethod
    def get_receipt(self) -> str:
        """Get receipt to be used for coffee drink."""


class LatteProduct(Product):
    """Get latte coffee drink product."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = None

    def get_receipt(self) -> Receipt:
        """Get latte coffee drink receipt."""
        return latte_receipt


class CappuccinoProduct(Product):
    """Get cappuccino coffee drink product."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = None

    def get_receipt(self) -> Receipt:
        """Get cappuccino coffee drink receipt."""
        return cappuccino_receipt


class EspressoProduct(Product):
    """Get espresso coffee drink product."""

    def __init__(self) -> None:
        self.contents = []
        self._receipt = None

    def get_receipt(self) -> Receipt:
        """Get espresso coffee drink receipt."""
        return espresso_receipt


def client_code(creator: CoffeeCreator) -> None:
    """Works with an instance of a concrete creator, albeit through its base interface.

    As long as the client keeps working with the creator via base interface, you can pass it any creator's subclass.
    Client: I'm not aware of the creator's class, but it still works.
    """
    creator.prepare()
