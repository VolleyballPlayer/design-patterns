import click
from designpatterns.utilities.package_resources import PackageResources

@click.group()
def cli():
    """
    Run structural patterns.
    """
    click.echo(f"Using design pattern package version {PackageResources.get_package_version()}")

@cli.command()
def run_adapter() -> None:
    """
    Run adapter example.

    This function calls adapter module to run an example of structural design pattern called adapter.
    """
    click.echo("This is adapter pattern")

if __name__ == "__main__":
    cli()
