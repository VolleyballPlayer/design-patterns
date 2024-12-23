import click

from designpatterns.creational_patterns.abstract_factory import (
    CappuccinoFactory,
    EspressoFactory,
    LatteFactory,
    client_code_abstract_factory,
)
from designpatterns.creational_patterns.builder import CappuccinoBuilder, Director, EspressoBuilder, LatteBuilder
from designpatterns.creational_patterns.factory_method import (
    CappuccinoCreator,
    EspressoCreator,
    LatteCreator,
    client_code_factory_method,
)
from designpatterns.creational_patterns.prototype import DoubleEspressoBuilderPrototype
from designpatterns.creational_patterns.singleton import CountCoffeeSingleton
from designpatterns.helpers.receipts import triple_espresso_receipt
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


@cli.command
def prototype() -> None:
    """Run prototype example.

    This function calls prototype module to run an example of creational design pattern called prototype.
    """
    logger.info('Starting prototype pattern run')

    director = Director()

    logger.info('Running cloned double espresso builder prototype')
    double_espresso_builder_clone = DoubleEspressoBuilderPrototype().clone()
    director.builder = double_espresso_builder_clone
    director.build_espresso()
    double_espresso_builder_clone.cup.list_contents()

    logger.info('Running original double espresso builder prototype without clone using triple espresso receipt')
    builder = DoubleEspressoBuilderPrototype()
    builder.receipt = triple_espresso_receipt
    director.builder = builder
    director.build_espresso()
    builder.cup.list_contents()

    logger.info('Running cloned double espresso builder prototype again - no impact of previous triple espresso run')
    director.builder = double_espresso_builder_clone
    director.build_espresso()
    double_espresso_builder_clone.cup.list_contents()

    logger.info('Running cloned espresso builder - no impact of prototypes')
    builder = EspressoBuilder()
    director.builder = builder
    director.build_espresso()
    builder.cup.list_contents()


@cli.command()
def factory_method() -> None:
    """Run factory method example.

    This function calls factory method module to run an example of creational design pattern called factory method.
    """
    logger.info('Starting factory method pattern run: your ordered coffees are about to be prepared.')

    client_code_factory_method(LatteCreator())
    client_code_factory_method(CappuccinoCreator())
    client_code_factory_method(EspressoCreator())


@cli.command()
def abstract_factory() -> None:
    """Run abstract factory example.

    This function calls abstract factory module to run an example of creational design pattern called abstract factory.
    """
    logger.info('Starting abstract factory pattern run: your ordered coffees are about to be prepared.')

    client_code_abstract_factory(LatteFactory())
    client_code_abstract_factory(CappuccinoFactory())
    client_code_abstract_factory(EspressoFactory())

if __name__ == '__main__':
    cli()
