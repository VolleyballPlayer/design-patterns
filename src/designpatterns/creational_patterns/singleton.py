from itertools import count

from designpatterns.logger import logger


class SingletonMeta(type):
    """Specify metaclass for Singleton class."""

    _instances = {}

    def __call__(cls, *args, **kwargs):  # noqa: ANN002, ANN003, ANN204
        """Apply call method so that changes to the value of the __init__ do not affect the returned instance."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CountCoffeeSingleton(metaclass=SingletonMeta):
    """Get number of ordered coffees."""

    _ids = count(1)

    def count(self) -> None:
        """Count number of ordered coffees."""
        self.id = next(self._ids)
        logger.info(f'{self.id}. coffee is being prepared')
