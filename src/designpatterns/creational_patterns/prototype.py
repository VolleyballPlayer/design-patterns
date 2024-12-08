from __future__ import annotations

import copy

from designpatterns.creational_patterns.builder import EspressoBuilder
from designpatterns.helpers.receipts import double_espresso_receipt


class DoubleEspressoBuilderPrototype(EspressoBuilder):
    """Provides specific implementations of the building steps of Double Espresso coffee drink."""

    def __init__(self) -> None:
        self.reset()
        self.receipt = double_espresso_receipt
        self.cup.receipt = double_espresso_receipt

    def clone(self) -> DoubleEspressoBuilderPrototype:
        """Return clone of the class such that changes in other instances do not effect prototype."""
        return copy.deepcopy(self)
