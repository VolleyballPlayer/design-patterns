import click

from designpatterns.helpers.receipts import latte_receipt
from designpatterns.logger import logger
from designpatterns.structural_patterns.adapter import Adaptee, Adapter, Target, client_code
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
    client_code(target)
    print('\n')

    adaptee = Adaptee(latte_receipt)
    logger.info('Client: The Adaptee class has a weird interface. ' 'See, it is not nicely formatted:')
    adaptee.get_coffee()
    print('\n')

    logger.info('Client: But I can work with it via the Adapter:')
    adapter = Adapter(adaptee)
    client_code(adapter)


if __name__ == '__main__':
    cli()
