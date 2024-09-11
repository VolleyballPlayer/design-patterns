from pathlib import Path
from importlib import metadata


class PackageResources:
    """
    Use this utility class to get information related to the package.
    """

    @staticmethod
    def get_project_root():
        """
        Get project root directory.
        """
        return Path(__file__).parent.parent
    
    @staticmethod
    def get_package_version():
        """
        Get latest version of package.
        """
        return metadata.version('designpatterns')