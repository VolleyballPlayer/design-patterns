from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import cappuccino_receipt, latte_receipt
from designpatterns.logger import logger


class Component(ABC):
    """The Component interface declares an `accept` method that should take the base visitor interface as argument."""

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        """Take the base visitor interface as argument."""


class LatteComponent(Component):
    """Each Concrete Component must implement the `accept` method in such a way that it calls the visitor's method.

    ...corresponding to the component's class.
    """

    def accept(self, visitor: Visitor) -> None:
        """Note that we're calling `visitConcreteComponentA`, which matches the current class name.

        This way we let the visitor know the class of the component it works with.
        """
        visitor.visit_latte_component(self)

    def exclusive_method_of_latte_component(self) -> str:
        """Concrete Components may have special methods that don't exist in their base class or interface.

        The Visitor is still able to use these methods since it's aware of the component's concrete class.
        """
        return latte_receipt


class CappuccinoComponent(Component):
    """Same here: visitConcreteComponentB => ConcreteComponentB."""

    def accept(self, visitor: Visitor) -> None:
        """Take the base visitor interface as argument."""
        visitor.visit_cappuccino_component(self)

    def special_method_of_cappuccino_component(self) -> str:
        """Add special method of cappuccino component."""
        return cappuccino_receipt


class Visitor(ABC):
    """The Visitor Interface declares a set of visiting methods that correspond to component classes.

    The signature of a visiting method allows the visitor to identify the exact class of the component that it's
    dealing with.
    """

    @abstractmethod
    def visit_latte_component(self, element: LatteComponent) -> None:
        """Define visit latte component."""

    @abstractmethod
    def visit_cappuccino_component(self, element: CappuccinoComponent) -> None:
        """Define visit cappuccino component."""


"""Concrete Visitors implement several versions of the same algorithm, which can work with all concrete component
classes. You can experience the biggest benefit of the Visitor pattern when using it with a complex object structure,
such as a Composite tree. In this case, it might be helpful to store some intermediate state of the algorithm while
executing visitor's methods over various objects of the structure.
"""


class CoffeeVisitor(Visitor):
    """Declare a set of visiting methods that correspond to coffee component classes."""

    def visit_latte_component(self, element: LatteComponent) -> None:
        """Define visit latte component."""
        logger.info('CoffeeVisitor for latte')
        logger.info(f'Latte contains {element.exclusive_method_of_latte_component().coffee}')

    def visit_cappuccino_component(self, element: CappuccinoComponent) -> None:
        """Define visit cappuccino component."""
        logger.info('CoffeeVisitor for cappuccino')
        logger.info(f'Cappuccino contains {element.special_method_of_cappuccino_component().coffee}')


class MilkVisitor(Visitor):
    """Declare a set of visiting methods that correspond to milk component classes."""

    def visit_latte_component(self, element: LatteComponent) -> None:
        """Define visit latte component."""
        logger.info('MilkVisitor for latte')
        logger.info(f'Latte contains {element.exclusive_method_of_latte_component().milk}')

    def visit_cappuccino_component(self, element: CappuccinoComponent) -> None:
        """Define visit cappuccino component."""
        logger.info('MilkVisitor for cappuccino')
        logger.info(f'Cappuccino contains {element.special_method_of_cappuccino_component().milk}')


def client_code(components: list[Component], visitor: Visitor) -> None:
    """Can run visitor operations over any set of elements without figuring out their concrete classes.

    The accept operation directs a call to the appropriate operation in the visitor object.
    """
    for component in components:
        component.accept(visitor)
