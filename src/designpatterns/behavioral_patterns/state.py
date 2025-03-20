from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.logger import logger


class State(ABC):
    """The base State class declares methods that all Concrete State should implement.

    It also provides a backreference to the Context object, associated with the State. This backreference can be used
    by States to transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        """Get current context."""
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def check_if_order_made(self, coffee: str) -> None:
        """Implement method to check if specific coffee order was already made."""

    @abstractmethod
    def prepare_coffee(self) -> None:
        """Prepare coffee."""


"""
Concrete States implement various behaviors, associated with a state of the Context.
"""


class Latte(State):
    """Implement latte state."""

    def check_if_order_made(self, coffee: str) -> None:
        """Implement method to check if latte coffee order was already made."""
        if coffee == 'latte':
            logger.info('Order was made for latte.')
        else:
            logger.info('Order was not made for latte. Check if it was made for cappuccino.')
            self.context.transition_to(Cappuccino())

    def prepare_coffee(self) -> None:
        """Prepare latte coffee."""
        logger.info('Preparing latte.')


class Cappuccino(State):
    """Implement cappuccino state."""

    def check_if_order_made(self, coffee: str) -> None:
        """Implement method to check if cappuccino coffee order was already made."""
        if coffee == 'cappuccino':
            logger.info('Order was made for cappuccino.')
        else:
            logger.info('Order was not made for cappuccino. Check if it was made for latte.')
            self.context.transition_to(Latte())

    def prepare_coffee(self) -> None:
        """Prepare cappuccino coffee."""
        logger.info('Preparing cappuccino')


class Context:
    """The Context defines the interface of interest to clients.

    It also maintains a reference to an instance of a State subclass, which represents the current state of the Context.
    """

    _state: State = Latte()

    """A reference to the current state of the Context."""

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        """Allow changing the State object at runtime."""
        logger.info(f'Context: Transition to {type(state).__name__}')
        self._state = state
        self._state.context = self

    """The Context delegates part of its behavior to the current State object."""

    def check_order(self, coffee: str) -> None:
        """Implement method to check if specific coffee order was already made."""
        self._state.check_if_order_made(coffee)

    def process_order(self) -> None:
        """Prepare specific coffee."""
        self._state.prepare_coffee()
