import datetime
from importlib import metadata
from pathlib import Path


class PackageResources:
    """Use this utility class to get information related to the package."""

    __PACKAGE_PATH = Path(__file__).parent.parent
    __PACKAGE_NAME = __PACKAGE_PATH.name

    @staticmethod
    def get_project_root() -> Path:
        """Get project root directory."""
        return PackageResources.__PACKAGE_PATH

    @staticmethod
    def get_package_version() -> str:
        """Get latest version of package."""
        return metadata.version(PackageResources.__PACKAGE_NAME)

    @staticmethod
    def create_package_version() -> None:
        """Get next package version for build."""
        current_month = datetime.datetime.now(tz=datetime.UTC).month
        current_year = datetime.datetime.now(tz=datetime.UTC).strftime('%y')
        __version__ = f'{current_year}.{current_month}'

        with Path.open(PackageResources.__PACKAGE_PATH / '__init__.py', 'w') as file:
            file.write(f"__version__ = '{__version__}'")
