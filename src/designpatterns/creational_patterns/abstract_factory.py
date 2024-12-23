from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, espresso_receipt, latte_receipt


class AbstractFactory(ABC):
    """The Abstract Factory interface declares a set of methods that return different abstract products.

    These products are called a family and are related by a high-level theme or concept.
    Products of one family are usually able to collaborate among themselves.
    A family of products may have several variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def get_coffee(self) -> AbstractCoffee:
        """Get coffee amount to be used for coffee drink."""

    @abstractmethod
    def get_milk(self) -> AbstractMilk:
        """Get milk amount to be used for coffee drink."""

    @abstractmethod
    def get_milk_foam(self) -> AbstractMilkFoam:
        """Get milk foam amount to be used for coffee drink."""

    @abstractmethod
    def get_chocolate(self) -> AbstractChocolate:
        """Get chocolate amount to be used for coffee drink."""

    @abstractmethod
    def get_coffee_receipt(self) -> AbstractReceipt:
        """Get coffee receipt to be used for coffee drink."""


class LatteFactory(AbstractFactory):
    """Concrete Factories produce a family of products that belong to a single variant.

    The factory guarantees that resulting products are compatible. Note that signatures of the Concrete Factory's
    methods return an abstract product, while inside the method a concrete product is instantiated.
    """

    def get_coffee(self) -> AbstractCoffee:
        """Get coffee amount to be used for latte coffee drink."""
        return CoffeeForLatte()

    def get_milk(self) -> AbstractMilk:
        """Get milk amount to be used for latte coffee drink."""
        return MilkForLatte()

    def get_milk_foam(self) -> AbstractMilkFoam:
        """Get milk foam amount to be used for latte coffee drink."""
        return MilkFoamForLatte()

    def get_chocolate(self) -> AbstractChocolate:
        """Get chocolate amount to be used for latte coffee drink."""
        return ChocolateForLatte()

    def get_coffee_receipt(self) -> AbstractReceipt:
        """Get coffee receipt to be used for latte coffee drink."""
        return ReceiptForLatte()


class CappuccinoFactory(AbstractFactory):
    """Concrete Factories produce a family of products that belong to a single variant.

    The factory guarantees that resulting products are compatible. Note that signatures of the Concrete Factory's
    methods return an abstract product, while inside the method a concrete product is instantiated.
    """

    def get_coffee(self) -> AbstractCoffee:
        """Get coffee amount to be used for cappuccino coffee drink."""
        return CoffeeForCappuccino()

    def get_milk(self) -> AbstractMilk:
        """Get milk amount to be used for cappuccino coffee drink."""
        return MilkForCappuccino()

    def get_milk_foam(self) -> AbstractMilkFoam:
        """Get milk foam amount to be used for cappuccino coffee drink."""
        return MilkFoamForCappuccino()

    def get_chocolate(self) -> AbstractChocolate:
        """Get chocolate amount to be used for cappuccino coffee drink."""
        return ChocolateForCappuccino()

    def get_coffee_receipt(self) -> AbstractReceipt:
        """Get coffee receipt to be used for cappuccino coffee drink."""
        return ReceiptForCappuccino()


class EspressoFactory(AbstractFactory):
    """Concrete Factories produce a family of products that belong to a single variant.

    The factory guarantees that resulting products are compatible. Note that signatures of the Concrete Factory's
    methods return an abstract product, while inside the method a concrete product is instantiated.
    """

    def get_coffee(self) -> AbstractCoffee:
        """Get coffee amount to be used for espresso coffee drink."""
        return CoffeeForEspresso()

    def get_milk(self) -> AbstractMilk:
        """Get milk amount to be used for espresso coffee drink."""
        return MilkForEspresso()

    def get_milk_foam(self) -> AbstractMilkFoam:
        """Get milk foam amount to be used for espresso coffee drink."""
        return MilkFoamForEspresso()

    def get_chocolate(self) -> AbstractChocolate:
        """Get chocolate amount to be used for espresso coffee drink."""
        return ChocolateForEspresso()

    def get_coffee_receipt(self) -> AbstractReceipt:
        """Get coffee receipt to be used for espresso coffee drink."""
        return ReceiptForEspresso()


class AbstractCoffee(ABC):
    """Each distinct product of a product family should have a base interface.

    All variants of the product must implement this interface.
    All products can interact with each other, but proper interaction is possible only between products of the same
    concrete variant.
    """

    @abstractmethod
    def get_amount(self) -> str:
        """Get coffee amount to be used for coffee drink."""


class CoffeeForLatte(AbstractCoffee):
    """Coffee to be used for latte coffee drink."""

    def get_amount(self) -> str:
        """Get coffee amount to be used for latte coffee drink."""
        return latte_receipt.coffee


class CoffeeForCappuccino(AbstractCoffee):
    """Coffee to be used for cappuccino coffee drink."""

    def get_amount(self) -> str:
        """Get coffee amount to be used for cappuccino coffee drink."""
        return cappuccino_receipt.coffee


class CoffeeForEspresso(AbstractCoffee):
    """Coffee to be used for espresso coffee drink."""

    def get_amount(self) -> str:
        """Get coffee amount to be used for espresso coffee drink."""
        return espresso_receipt.coffee


class AbstractMilk(ABC):
    """Each distinct product of a product family should have a base interface.

    All variants of the product must implement this interface.
    """

    @abstractmethod
    def get_amount(self) -> str:
        """Get milk amount to be used for coffee drink."""


class MilkForLatte(AbstractCoffee):
    """Milk to be used for latte coffee drink."""

    def get_amount(self) -> str:
        """Get milk amount to be used for latte coffee drink."""
        return latte_receipt.milk


class MilkForCappuccino(AbstractCoffee):
    """Milk to be used for cappuccino coffee drink."""

    def get_amount(self) -> str:
        """Get milk amount to be used for cappuccino coffee drink."""
        return cappuccino_receipt.milk


class MilkForEspresso(AbstractCoffee):
    """Milk to be used for espresso coffee drink."""

    def get_amount(self) -> str:
        """Get milk amount to be used for espresso coffee drink."""
        return espresso_receipt.milk


class AbstractMilkFoam(ABC):
    """Each distinct product of a product family should have a base interface.

    All variants of the product must implement this interface.
    """

    @abstractmethod
    def get_amount(self) -> str:
        """Get milk foam amount to be used for coffee drink."""


class MilkFoamForLatte(AbstractCoffee):
    """Milk foam to be used for latte coffee drink."""

    def get_amount(self) -> str:
        """Get milk foam amount to be used for latte coffee drink."""
        return latte_receipt.milk_foam


class MilkFoamForCappuccino(AbstractCoffee):
    """Milk foam to be used for cappuccino coffee drink."""

    def get_amount(self) -> str:
        """Get milk foam amount to be used for cappuccino coffee drink."""
        return cappuccino_receipt.milk_foam


class MilkFoamForEspresso(AbstractCoffee):
    """Milk foam to be used for espresso coffee drink."""

    def get_amount(self) -> str:
        """Get milk foam amount to be used for espresso coffee drink."""
        return espresso_receipt.milk_foam


class AbstractChocolate(ABC):
    """Each distinct product of a product family should have a base interface.

    All variants of the product must implement this interface.
    """

    @abstractmethod
    def get_amount(self) -> str:
        """Get chocolate amount to be used for coffee drink."""


class ChocolateForLatte(AbstractCoffee):
    """Chocolate to be used for latte coffee drink."""

    def get_amount(self) -> str:
        """Get chocolate amount to be used for latte coffee drink."""
        return latte_receipt.chocolate


class ChocolateForCappuccino(AbstractCoffee):
    """Chocolate to be used for cappuccino coffee drink."""

    def get_amount(self) -> str:
        """Get chocolate amount to be used for cappuccino coffee drink."""
        return cappuccino_receipt.chocolate


class ChocolateForEspresso(AbstractCoffee):
    """Chocolate to be used for espresso coffee drink."""

    def get_amount(self) -> str:
        """Get chocolate amount to be used for espresso coffee drink."""
        return espresso_receipt.chocolate


class AbstractReceipt(ABC):
    """Each distinct product of a product family should have a base interface.

    All variants of the product must implement this interface.
    """

    @abstractmethod
    def get_receipt(self) -> str:
        """Get receipt to be used for coffee drink."""


class ReceiptForLatte(AbstractReceipt):
    """Receipt to be used for latte coffee drink."""

    def get_receipt(self) -> str:
        """Get receipt to be used for latte coffee drink."""
        return latte_receipt


class ReceiptForCappuccino(AbstractReceipt):
    """Receipt to be used for cappuccino coffee drink."""

    def get_receipt(self) -> str:
        """Get receipt amount to be used for cappuccino coffee drink."""
        return cappuccino_receipt


class ReceiptForEspresso(AbstractReceipt):
    """Receipt to be used for espresso coffee drink."""

    def get_receipt(self) -> str:
        """Get receipt amount to be used for espresso coffee drink."""
        return espresso_receipt


def client_code_abstract_factory(factory: AbstractFactory) -> None:
    """Works with factories and products only through abstract types:AbstractFactory and AbstractProduct.

    This lets you pass any factory or product subclass to the client code without breaking it.
    """
    coffee = factory.get_coffee()
    milk = factory.get_milk()
    milk_foam = factory.get_milk_foam()
    chocolate = factory.get_chocolate()
    receipt = factory.get_coffee_receipt()

    ingredients = [coffee.get_amount(), milk.get_amount(), milk_foam.get_amount(), chocolate.get_amount()]
    Receipt.get_coffee(receipt=receipt.get_receipt(), ingredients=ingredients)
