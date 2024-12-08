import click

from designpatterns.creational_patterns.builder import CappuccinoBuilder, Director, EspressoBuilder, LatteBuilder
from designpatterns.creational_patterns.singleton import CountCoffeeSingleton
from designpatterns.logger import logger
from designpatterns.utilities.package_resources import PackageResources


@click.group()
def cli() -> None:
    """Run creational patterns."""
    logger.info(f'Using design patterns package version {PackageResources.get_package_version()}.')


@cli.command()
def builder() -> None:
    """Run builder example.

    This function calls builder module to run an example of creational design pattern called builder.
    """
    logger.info('Starting builder pattern run: your ordered coffees are about to be prepared.')

    director = Director()

    builder = LatteBuilder()
    director.builder = builder
    director.build_latte()
    builder.cup.list_contents()

    builder = CappuccinoBuilder()
    director.builder = builder
    director.build_cappuccino()
    builder.cup.list_contents()

    builder = EspressoBuilder()
    director.builder = builder
    director.build_espresso()
    builder.cup.list_contents()


@cli.command()
def singleton() -> None:
    """Run singleton example.

    This function calls singleton module to run an example of creational design pattern called singleton.
    """
    logger.info('Starting singleton pattern run')

    s1 = CountCoffeeSingleton().count()
    s2 = CountCoffeeSingleton().count()

    if id(s1) == id(s2):
        logger.info('Prepared coffees are counted by the same singleton instance.')
    else:
        logger.info('Singleton failed, variables contain different instances.')


if __name__ == '__main__':
    cli()
