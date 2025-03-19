from abc import ABC, abstractmethod
import datetime

import pytz

from designpatterns.helpers.receipts import Receipt
from designpatterns.logger import logger


class Subject(ABC):
    """The Subject interface declares common operations for both RealSubject and the Proxy.

    As long as the client works with RealSubject using this interface, you'll be able to pass it a proxy instead of a
    real subject.
    """

    @abstractmethod
    def request(self, receipt: Receipt) -> None:
        """Get coffee."""
        pass


class Coffee(Subject):
    """The RealSubject contains some core business logic.

    Usually, RealSubjects are capable of doing some useful work which may also be very slow or sensitive - e.g.
    correcting input data. A Proxy can solve these issues without any changes to the RealSubject's code.
    """

    def request(self, receipt: Receipt) -> None:
        """Get coffee."""
        Receipt.get_coffee(receipt=receipt)


class Proxy(Subject):
    """The Proxy has an interface identical to the RealSubject."""

    def __init__(self, real_subject: Coffee) -> None:
        self._real_subject = real_subject
        self._cache = {}

    def request(self, receipt: Receipt) -> None:
        """Use of the Proxy pattern like lazy loading, caching, controlling the access, logging, etc.

        A Proxy can perform one of these things and then, depending on the result, pass the execution to the same
        method in a linked RealSubject object.
        """
        if self.should_prepare_coffee(receipt):
            self._real_subject.request(receipt)
            self.log_access()
        else:
            logger.info('Latte was already prepared.')

    def should_prepare_coffee(self, receipt: Receipt) -> bool:
        """Check if hashed subject instance exists."""
        logger.info('Proxy: Checking if subject instance already exists to reuse cached instance.')
        if receipt in self._cache:
            should_prepare_coffee = False
        else:
            self._cache[receipt] = receipt
            should_prepare_coffee = True
        return should_prepare_coffee

    def log_access(self) -> None:
        """Log time of coffee preparation."""
        logger.info(
            f"Proxy: Logging the time of request {datetime.datetime.now(tz=pytz.timezone('Europe/Vienna')).time()}"
        )


def client_code(subject: Subject, receipt: Receipt) -> None:
    """Work with all objects (subjects and proxies) via the Subject interface to support both real subjects and proxies.

    In real life, however, clients mostly work with their real subjects directly. In this case, to implement the pattern
    more easily, you can extend your proxy from the real subject's class.
    """
    # ...

    subject.request(receipt)

    # ...
