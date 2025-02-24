from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt
from designpatterns.logger import logger


class AbstractClass(ABC):
    """The Abstract Class defines a template method that contains a skeleton of some algorithm.

    Skeleton is composed of calls to (usually) abstract primitive operations.
    Concrete subclasses should implement these operations, but leave the template method itself intact.
    """

    def template_method(self) -> None:
        """Define the skeleton of an algorithm."""
        self.get_coffee_order()
        self.process_coffee_order()
        self.assign_order_to_employee()
        self.hook1()
        self.prepare_coffee()
        self.finalize_order()
        self.hook2()

    def get_coffee_order(self) -> None:
        """Get coffee order."""
        logger.info('Automat says: I am receiving coffee order')

    def assign_order_to_employee(self) -> None:
        """Assign order to an employee."""
        logger.info('Automat says: Your order will be prepared by Maria')

    def finalize_order(self) -> None:
        """Provide information about completion to a client."""
        logger.info('Automat says: Your order is ready')

    @abstractmethod
    def process_coffee_order(self) -> None:
        """Specify which coffee is being ordered."""

    @abstractmethod
    def prepare_coffee(self) -> None:
        """Prepare specific coffee drink."""

    # These are "hooks." Subclasses may override them, but it's not mandatory
    # since the hooks already have default (but empty) implementation. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.

    def hook1(self) -> None:  # noqa: B027
        """Set additional extension point."""

    def hook2(self) -> None:  # noqa: B027
        """Set additional extension point."""


class Latte(AbstractClass):
    """Concrete classes have to implement all abstract operations of the base class.

    They can also override some operations with a default implementation.
    """

    def process_coffee_order(self) -> None:
        """Specify which coffee is being ordered."""
        logger.info(f'Your {latte_receipt.name} order is being prepared')

    def prepare_coffee(self) -> None:
        """Prepare specific coffee drink."""
        Receipt.get_coffee(latte_receipt)


class Cappuccino(AbstractClass):
    """Usually, concrete classes override only a fraction of base class operations."""

    def process_coffee_order(self) -> None:
        """Specify which coffee is being ordered."""
        logger.info(f'Your {cappuccino_receipt.name} order is being prepared')

    def prepare_coffee(self) -> None:
        """Prepare specific coffee drink."""
        Receipt.get_coffee(cappuccino_receipt)

    def hook1(self) -> None:
        """Implement additional steps."""
        logger.info('Maria forwarded order to a colleague Pedro')


def client_code(abstract_class: AbstractClass) -> None:
    """Call the template method to execute the algorithm.

    Client code does not have to know the concrete class of an object it works with, as long as it works with objects
    through the interface of their base class.
    """
    abstract_class.template_method()
