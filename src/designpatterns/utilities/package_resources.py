from importlib import metadata
from pathlib import Path


class PackageResources:
	"""
	Use this utility class to get information related to the package.
	"""

	@staticmethod
	def get_project_root() -> Path:
		"""
		Get project root directory.
		"""
		return Path(__file__).parent.parent

	@staticmethod
	def get_package_version() -> str:
		"""
		Get latest version of package.
		"""
		return metadata.version('designpatterns')
