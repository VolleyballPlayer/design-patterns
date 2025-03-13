from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt, latte_receipt
from designpatterns.logger import logger


class Component(ABC):
    """The base Component interface defines operations that can be altered by decorators."""

    @abstractmethod
    def operation(self) -> None:
        """Define get coffee method."""


class PrepareLatte(Component):
    """Concrete Components provide default implementations of the operations.

    There might be several variations of these classes.
    """

    def operation(self) -> None:
        """Define get coffee method."""
        Receipt.get_coffee(receipt=latte_receipt)


class Decorator(Component):
    """The base Decorator class follows the same interface as the other components.

    The primary purpose of this class is to define the wrapping interface for all concrete decorators.
    The default implementation of the wrapping code might include a field for storing a wrapped component and the means
    to initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """The Decorator delegates all work to the wrapped component."""
        return self._component

    def operation(self) -> None:
        """Define get coffee method."""
        return self._component.operation()


class Notification(Decorator):
    """Concrete Decorators call the wrapped object and alter its result in some way."""

    def operation(self) -> str:
        """May call parent implementation of the operation, instead of calling the wrapped object directly.

        This approach simplifies extension of decorator classes.
        """
        logger.info('Latte is prepared')


class Payment(Decorator):
    """Decorators can execute their behavior either before or after the call to a wrapped object."""

    def operation(self) -> None:
        """Request payment."""
        logger.info('Your coffee costs €5. Do you want to pay by cash or card?')


def client_code(component: Component) -> None:
    """Work with all objects using the Component interface.

    This way it can stay independent of the concrete classes of components it works with.
    """
    component.operation()
