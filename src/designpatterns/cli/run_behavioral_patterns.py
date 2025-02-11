import click

from designpatterns.behavioral_patterns.observer import (
    DiscountSubject,
    ObserverWeekendDiscounts,
    ObserverWorkDayDiscounts,
)
from designpatterns.behavioral_patterns.strategy import (
    Context,
    StrategyCappuccino,
    StrategyEspresso,
    StrategyLatte,
)
from designpatterns.logger import logger
from designpatterns.utilities.package_resources import PackageResources


@click.group()
def cli() -> None:
    """Run behavioral patterns."""
    logger.info(f'Using design patterns package version {PackageResources.get_package_version()}')


@cli.command()
def strategy() -> None:
    """Run strategy example.

    This function calls strategy module to run an example of behavioral design pattern called strategy.
    """
    logger.info('Starting strategy pattern run')

    context = Context(StrategyLatte())
    context.prepare_coffee()

    context.strategy = StrategyCappuccino()
    context.prepare_coffee()

    context.strategy = StrategyEspresso()
    context.prepare_coffee()


@cli.command()
def observer() -> None:
    """Run observer example.

    This function calls observer module to run an example of behavioral design pattern called observer.
    """
    logger.info('Starting observer pattern run')

    subject = DiscountSubject()

    observer_a = ObserverWorkDayDiscounts()
    subject.attach(observer_a)
    observer_b = ObserverWorkDayDiscounts()
    subject.attach(observer_b)

    observer_c = ObserverWeekendDiscounts()
    subject.attach(observer_c)

    subject.send_discounts()

    subject.detach(observer_a)

    subject.send_discounts()


if __name__ == '__main__':
    cli()
