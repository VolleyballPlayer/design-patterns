from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any

"""
To create an iterator in Python, there are two abstract classes from the built-in `collections` module - Iterable,
Iterator. We need to implement the `__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""


class ExpenseOrderIterator(Iterator):
    """Concrete Iterators implement various traversal algorithms.

    These classes store the current traversal position at all times.
    """

    """
    `_position` attribute stores the current traversal position. An iterator may have a lot of other fields for storing
    iteration state, especially when it is supposed to work with a particular kind of collection.
    """
    _position: int = None

    """This attribute indicates the traversal direction."""
    _reverse: bool = False

    def __init__(self, collection: PriceCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:  # noqa: ANN401
        """Return the next item in the sequence (its a must).

        On reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration() from None

        return value


class PriceCollection(Iterable):
    """Concrete Collections provide one or several methods for retrieving fresh iterator instances.

    ...compatible with the collection class.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:  # noqa: ANN401
        """Get collection item."""
        return self._collection[index]

    def __iter__(self) -> ExpenseOrderIterator:
        """Return the iterator object itself.

        By default we return the iterator in ascending order.
        """
        return ExpenseOrderIterator(self)

    def get_reverse_iterator(self) -> ExpenseOrderIterator:
        """Get iterator in reverse order."""
        return ExpenseOrderIterator(self, True)

    def add_item(self, item: Any) -> None:  # noqa: ANN401
        """Add an item to the collection."""
        self._collection.append(item)
