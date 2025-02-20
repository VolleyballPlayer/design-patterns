from abc import ABC, abstractmethod
from enum import Enum

from designpatterns.logger import logger


class OrderStatus(Enum):
    """Enum class for status."""

    NO_ORDER = 1
    ORDERED = 2
    PREPARED = 3
    PAID = 4


class Mediator(ABC):
    """Mediator interface declares communication methods."""

    @abstractmethod
    def notify(self) -> None:
        """Notify method for sending messages to components."""


class BaseComponent:
    """Provide the basic functionality of storing a mediator's instance inside component objects."""

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        """Get mediator."""
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        """Set mediator."""
        self._mediator = mediator


class ConcreteMediator(Mediator):
    """Concrete Mediator manages communication between components."""

    def __init__(self) -> None:
        self._components = []
        self._status = OrderStatus.NO_ORDER

    def add_component(self, component: BaseComponent) -> None:
        """Add a component to the mediator."""
        self._components.append(component)

    @property
    def status(self) -> OrderStatus:
        """Get order status."""
        return self._status

    @status.setter
    def status(self, status: OrderStatus) -> None:
        """Set order status."""
        self._status = status

    def notify(self) -> None:
        """Notify all components with the message."""
        if self.status == OrderStatus.ORDERED:
            message = 'Order is ready.'
        elif self.status == OrderStatus.PREPARED:
            message = 'Coffee is ready.'
        elif self.status == OrderStatus.PAID:
            message = 'Payment is processed.'
        else:
            message = 'No order has been made yet.'

        for component in self._components:
            component.inform(message)


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Order(BaseComponent):
    """Represents a component with business logic."""

    def process(self, coffee: str) -> None:
        """Send a message to the mediator."""
        logger.info(f'Receiving order for {coffee} coffee.')

        self._mediator.status = OrderStatus.ORDERED
        self._mediator.notify()

    def inform(self, message: str) -> None:
        """Receives and processes messages from the mediator."""
        logger.info(f'Order component received message: {message}')


class Coffee(BaseComponent):
    """Represents a component with business logic."""

    def prepare(self, coffee: str) -> None:
        """Send a message to the mediator."""
        logger.info(f'Preparing {coffee} coffee.')

        self._mediator.status = OrderStatus.PREPARED
        self._mediator.notify()

    def inform(self, message: str) -> None:
        """Receives and processes messages from the mediator."""
        logger.info(f'Coffee component received message: {message}')


class Payment(BaseComponent):
    """Represents a component with business logic."""

    def receive(self, coffee: str) -> None:
        """Send a message to the mediator."""
        logger.info(f'Receiving payment for {coffee} coffee.')

        self._mediator.status = OrderStatus.PAID
        self._mediator.notify()

    def inform(self, message: str) -> None:
        """Receives and processes messages from the mediator."""
        logger.info(f'Payment component received message: {message}')
