from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.helpers.receipts import Receipt
from designpatterns.logger import logger


class Command(ABC):
    """The Command interface declares a method for executing a command."""

    @abstractmethod
    def execute(self) -> None:
        """Execute command."""


class OrderCommand(Command):
    """Some commands can implement simple operations on their own."""

    def __init__(self, receipt: str) -> None:
        self._receipt = receipt

    def execute(self) -> None:
        """Execute command."""
        logger.info(
            f'Simple Command: See, I can do simple things like receiving order for {self._receipt.name} coffee.'
        )


class PrepareCoffeeCommand(Command):
    """However, some commands can delegate more complex operations to other objects, called 'receivers'."""

    def __init__(self, receiver: Receiver, receipt: Receipt, customer: str) -> None:
        """Complex commands can accept one or several receiver objects along with any context data via constructor."""
        self._receiver = receiver
        self._receipt = receipt
        self._customer = customer

    def execute(self) -> None:
        """Commands can delegate to any methods of a receiver."""
        logger.info('Complex Command: Complex stuff should be done by a receiver object')
        self._receiver.prepare_coffee(self._receipt)
        self._receiver.inform_buyer(self._customer)


class Receiver:
    """The Receiver classes contain some important business logic.

    They know how to perform all kinds of operations, associated with carrying out a request. In fact,
    any class may serve as a Receiver.
    """

    def prepare_coffee(self, receipt: Receipt) -> None:
        """Get which coffee is made with which ingredients."""
        logger.info(f'Receiver: Preparing {receipt.name}')
        receipt.get_coffee(receipt)

    def inform_buyer(self, customer: str) -> None:
        """Inform buyer when his coffee is ready."""
        logger.info(f'Receiver: {customer}, your coffee is ready.')


class Invoker:
    """The Invoker is associated with one or several commands. It sends a request to the command."""

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command) -> None:
        """Set a command to be run on start."""
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        """Set a command to be run on finish."""
        self._on_finish = command

    def execute_commands_in_order(self) -> None:
        """Do not depend on concrete command or receiver classes (referring to Invoker).

        The Invoker passes a request to a receiver indirectly, by executing a command.
        """
        logger.info('Invoker: Does anybody want something done before I begin?')
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        logger.info('Invoker: ...doing steps in between...like giving receipt, processing order, etc.')

        logger.info('Invoker: Does anybody want something done after I finish?')
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
