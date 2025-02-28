import click

from designpatterns.behavioral_patterns.command import Receiver
from designpatterns.helpers.receipts import latte_receipt
from designpatterns.logger import logger
from designpatterns.structural_patterns.adapter import (
    Adaptee,
    Adapter,
    Target,
    client_code as client_code_adapter,
)
from designpatterns.structural_patterns.bridge import (
    Abstraction,
    Cappuccino,
    Coffee,
    Latte,
    client_code as client_code_bridge,
)
from designpatterns.structural_patterns.composite import (
    Composite,
    Leaf,
    client_code as client_code_composite,
    client_code2 as client_code_composite2,
)
from designpatterns.structural_patterns.facade import (
    ExtendedOrderCommand,
    ExtendedPrepareCoffeeCommand,
    Facade,
    client_code as client_code_facade,
)
from designpatterns.utilities.package_resources import PackageResources


@click.group()
def cli() -> None:
    """Run structural patterns."""
    logger.info(f'Using design patterns package version {PackageResources.get_package_version()}')


@cli.command()
def adapter() -> None:
    """Run adapter example.

    This function calls adapter module to run an example of structural design pattern called adapter.
    """
    logger.info('Client: I can work just fine with the Target objects:')
    target = Target()
    client_code_adapter(target)
    print('\n')

    adaptee = Adaptee(latte_receipt)
    logger.info('Client: The Adaptee class has a weird interface. ' 'See, it is not nicely formatted:')
    adaptee.get_coffee()
    print('\n')

    logger.info('Client: But I can work with it via the Adapter:')
    adapter = Adapter(adaptee)
    client_code_adapter(adapter)


@cli.command()
def facade() -> None:
    """Run facade example.

    This function calls facade module to run an example of structural design pattern called facade.
    """
    logger.info('Starting facade pattern run')

    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.

    subsystem1 = ExtendedOrderCommand(latte_receipt)
    subsystem2 = ExtendedPrepareCoffeeCommand(Receiver(), latte_receipt, 'John Smith')
    facade = Facade(subsystem1, subsystem2)
    client_code_facade(facade)


@cli.command()
def bridge() -> None:
    """Run bridge example.

    This function calls bridge module to run an example of structural design pattern called bridge.
    """
    logger.info('Starting bridge pattern run')

    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """
    implementation = Latte()
    abstraction = Abstraction(implementation)
    client_code_bridge(abstraction)

    print('\n')

    implementation = Cappuccino()
    abstraction = Coffee(implementation)
    client_code_bridge(abstraction)


@cli.command()
def composite() -> None:
    """Run composite example.

    This function calls composite module to run an example of structural design pattern called composite.
    """
    logger.info('Starting composite pattern run')

    simple = Leaf('Water: €0')
    print("Client: I've got a simple component:")
    client_code_composite(simple)
    print('\n')

    tree = Composite('Coffees')

    big_coffees = Composite('Big Coffees')
    big_coffees.add(Leaf('Cappuccino: €4'))
    big_coffees.add(Leaf('Latte: €5'))

    small_coffees = Composite('Small Coffees')
    small_coffees.add(Leaf('Espresso: €1'))
    small_coffees.add(Leaf('Double Espresso: €2'))
    small_coffees.add(Leaf('Triple Espresso: €3'))

    tree.add(big_coffees)
    tree.add(small_coffees)

    print("Client: Now I've got a composite tree:")
    client_code_composite(tree)
    print('\n')

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code_composite2(tree, simple)


if __name__ == '__main__':
    cli()
