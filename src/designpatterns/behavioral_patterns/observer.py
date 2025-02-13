from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

import pytz

from designpatterns.logger import logger


class Publisher(ABC):
    """The Publisher interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the publisher."""

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the publisher."""

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event."""


class DiscountPublisher(Publisher):
    """The Publisher owns some important state and notifies observers when the state changes."""

    _state: str = None
    """For the sake of simplicity, the Publisher's state, essential to all subscribers, is stored in this variable."""

    _observers: list[Observer] = []
    """List of subscribers. In real life, the list of subscribers can be stored more comprehensively
    (categorized by event type, etc.).
    """

    @property
    def state(self) -> str:
        """Get state property."""
        return self._state

    def attach(self, observer: Observer) -> None:
        """Attach observers."""
        logger.info('Publisher: Attached an observer.')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach observers."""
        self._observers.remove(observer)

    """The subscription management methods."""

    def notify(self) -> None:
        """Trigger an update in each subscriber."""
        logger.info('Publisher: Notifying observers...')
        if self._observers:
            for observer in self._observers:
                observer.update(self)
        else:
            logger.info('No subscribed observers.')

    def send_discounts(self) -> None:
        """Usually, the subscription logic is only a fraction of what a Publisher can really do.

        Publishers commonly hold some important business logic, that triggers a notification method whenever something
        important is about to happen (or after it).
        """
        logger.info("Publisher: I'm checking available discounts.")
        week_day_number = datetime.now(tz=pytz.timezone('Europe/Vienna')).weekday()
        self._state = 'workday' if week_day_number < 5 else 'weekend'
        logger.info(f'Publisher: My state has just changed to: {self._state}')
        self.notify()


class Observer(ABC):
    """The Observer interface declares the update method, used by publishers."""

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        """Receive update from publisher."""


"""Concrete Observers react to the updates issued by the Publisher they had been attached to."""


class ObserverWorkDayDiscounts(Observer):
    """Update subscribed customer on work day discounts."""

    def update(self, publisher: Publisher) -> None:
        """Inform observer about discounts."""
        if publisher.state == 'workday':
            logger.info(r'This week latte coffee has 50% discount')


class ObserverWeekendDiscounts(Observer):
    """Update subscribed customers on weekend discount."""

    def update(self, publisher: Publisher) -> None:
        """Inform observer about discounts."""
        if publisher.state == 'weekend':
            logger.info(r'This weekend cappuccino coffee has 30% discount')
