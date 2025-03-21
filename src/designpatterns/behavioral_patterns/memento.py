from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

import pytz

from designpatterns.logger import logger


class Originator:
    """The Originator holds some important state that may change over time.

    It also defines a method for saving the state inside a memento and another method for restoring the state from it.
    """

    _state = None
    """For the sake of simplicity, the originator's state is stored inside a single variable."""

    def __init__(self, state: str) -> None:
        self._state = state
        logger.info(f'Originator: My initial state is: {self._state}')

    def receive_order(self, coffee: str) -> None:
        """May affect its internal state.

        Therefore, the client should backup the state before launching methods of the business logic via the save()
        method.
        """
        logger.info("Originator: I'm checking the next order.")
        self._state = self._get_coffee_order(coffee)
        logger.info(f'Originator: and my state has changed to: {self._state}')

    @staticmethod
    def _get_coffee_order(coffee: str) -> str:
        logger.info(f'Received an order for {coffee} coffee drink')
        return coffee

    def save(self) -> Memento:
        """Save the current state inside a memento."""
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """Restores the Originator's state from a memento object."""
        self._state = memento.get_state()
        logger.info(f'Originator: My state has changed to: {self._state}')


class Memento(ABC):
    """The Memento interface provides a way to retrieve the memento's metadata, such as creation date or name.

    However, it doesn't expose the Originator's state.
    """

    @abstractmethod
    def get_name(self) -> str:
        """Get memento name."""

    @abstractmethod
    def get_date(self) -> str:
        """Get memento date."""


class ConcreteMemento(Memento):
    """Implement memento."""

    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now(tz=pytz.timezone('Europe/Vienna')))[:19]

    def get_state(self) -> str:
        """Use this method when restoring its state in originator."""
        return self._state

    def get_name(self) -> str:
        """Display metadata."""
        return f'{self._date} / {self._state}'

    def get_date(self) -> str:
        """Get date."""
        return self._date


class Caretaker:
    """The Caretaker doesn't depend on the Concrete Memento class.

    Therefore, it doesn't have access to the originator's state, stored inside the memento. It works with all mementos
    via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        """Backup originator state."""
        logger.info("Caretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        """Restoring state."""
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        logger.info(f'Caretaker: Restoring state to: {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        """Show list of mementos."""
        logger.info("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())
