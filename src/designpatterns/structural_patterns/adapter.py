from tabulate import tabulate

from designpatterns.helpers.receipts import Receipt


class Target:
    """The Target defines the domain-specific interface used by the client code."""

    def print(self, input: str = "Target: The default target's behavior.") -> str:
        """Print string input as a table."""
        print(tabulate([[input]], tablefmt='psql'))


class Adaptee:
    """The Adaptee contains some useful behavior, but its interface is incompatible with the existing client code.

    The Adaptee needs some adaptation before the client code can use it.
    """

    def __init__(self, receipt: Receipt) -> None:
        self._receipt = receipt

    @property
    def receipt(self) -> Receipt:
        """Get receipt."""
        return self._receipt

    def get_coffee(self) -> str:
        """Get which coffee is made with which ingredients."""
        return Receipt.get_coffee(self._receipt)


class Adapter(Target):
    """The Adapter makes the Adaptee's interface compatible with the Target's interface via composition."""

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def print(self) -> str:
        """Print coffee ingredients as a table."""
        receipt = self.adaptee.receipt
        ingredients = receipt.get_ingredients()
        print(tabulate([[receipt.name]], tablefmt='psql'))
        print(tabulate([ingredients], tablefmt='psql'))


def client_code(target: Target) -> None:
    """Support all classes that follow the Target interface."""
    target.print()
