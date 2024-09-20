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
    def increment_package_version() -> None:
        """Get next package version for build."""
        __version__ = metadata.version(PackageResources.__PACKAGE_NAME)
        __version__ = __version__.split('.')

        increment = str(int(__version__[2]) + 1)

        __version__ = f'{__version__[0]}.{__version__[1]}.{increment}'

        with Path.open(PackageResources.__PACKAGE_PATH / '__init__.py', 'w') as file:
            file.write(f"__version__ = '{__version__}'")
