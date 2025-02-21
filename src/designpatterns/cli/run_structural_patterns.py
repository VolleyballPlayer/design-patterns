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


if __name__ == '__main__':
    cli()
