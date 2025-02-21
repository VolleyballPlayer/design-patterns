from __future__ import annotations

from designpatterns.behavioral_patterns.command import OrderCommand, PrepareCoffeeCommand
from designpatterns.logger import logger


class Facade:
    """The Facade class provides a simple interface to the complex logic of one or several subsystems.

    The Facade delegates the client requests to the appropriate objects within the subsystem.
    The Facade is also responsible for managing their lifecycle.
    All of this shields the client from the undesired complexity of the subsystem.
    """

    def __init__(self, subsystem1: OrderCommand, subsystem2: PrepareCoffeeCommand) -> None:
        """You can provide the Facade with existing subsystem objects or force the Facade to create them on its own."""
        self._subsystem1 = subsystem1 or ExtendedOrderCommand()
        self._subsystem2 = subsystem2 or ExtendedPrepareCoffeeCommand()

    def operation(self) -> str:
        """Be convenient shortcut to the sophisticated functionality of the subsystems.

        However, clients get only to a fraction of a subsystem's capabilities.
        """
        logger.info('Facade initializes subsystems:')
        self._subsystem1.execute()
        logger.info('Facade orders subsystems to perform the action:')
        self._subsystem1.forward_order_details()
        self._subsystem2.execute()
        self._subsystem2.get_payment()


class ExtendedOrderCommand(OrderCommand):
    """The Subsystem can accept requests either from the facade or client directly.

    In any case, to the Subsystem, the Facade is yet another client, and it's not a part of the Subsystem.
    """

    def forward_order_details(self) -> str:
        """Forward order details to restaurant stuff."""
        logger.info('Please find order details')


class ExtendedPrepareCoffeeCommand(PrepareCoffeeCommand):
    """Some facades can work with multiple subsystems at the same time."""

    def get_payment(self) -> str:
        """Get payment from customer."""
        logger.info('Your coffee costs €2. This is your bill.')


def client_code(facade: Facade) -> None:
    """Works with complex subsystems through a simple interface provided by the Facade.

    When a facade manages the lifecycle of the subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """
    facade.operation()
