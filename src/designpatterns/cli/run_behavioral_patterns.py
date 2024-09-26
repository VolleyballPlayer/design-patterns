import click

from designpatterns.logger import logger
from designpatterns.utilities.package_resources import PackageResources


@click.group()
def cli() -> None:
    """Run behavioral patterns."""
    logger.info(f'Using design patterns package version {PackageResources.get_package_version()}')


@cli.command()
def command() -> None:
    """Run command example.

    This function calls command module to run an example of behavioral design pattern called command.
    """
    logger.info('This is command pattern')


if __name__ == '__main__':
    cli()
