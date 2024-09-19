import click
from designpatterns.utilities.package_resources import PackageResources
from designpatterns.logger import logger

@click.group()
def cli():
    """
    Run structural patterns.
    """
    logger.info(f"Using design pattern package version {PackageResources.get_package_version()}")

@cli.command()
def run_adapter() -> None:
    """ 
    Run adapter example.

    This function calls adapter module to run an example of structural design pattern called adapter.
    """
    logger.info("This is adapter pattern")

if __name__ == "__main__":
    cli()