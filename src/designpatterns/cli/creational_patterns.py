import click
from designpatterns.utilities.package_resources import PackageResources

@click.group()
def cli():
    """
    Run creational patterns.
    """
    click.echo(f"Using design pattern package version {PackageResources.get_package_version()}")

@cli.command()
def run_builder() -> None:
    """
    Run builder example.

    This function calls builder module to run an example of creational design pattern called builder.
    """
    click.echo("This is builder pattern")

@cli.command()
def run_singleton() -> None:
    """
    Run singleton example.

    This function calls singleton module to run an example of creational design pattern called singleton.
    """
    click.echo("This is singleton pattern")

if __name__ == "__main__":
    cli()
