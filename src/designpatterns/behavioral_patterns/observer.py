from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

import pytz

from designpatterns.logger import logger


class Subject(ABC):
    """The Subject interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event."""


class DiscountSubject(Subject):
    """The Subject owns some important state and notifies observers when the state changes."""

    _state: str = None
    """For the sake of simplicity, the Subject's state, essential to all subscribers, is stored in this variable."""

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
        logger.info('Subject: Attached an observer.')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach observers."""
        self._observers.remove(observer)

    """The subscription management methods."""

    def notify(self) -> None:
        """Trigger an update in each subscriber."""
        logger.info('Subject: Notifying observers...')
        if self._observers:
            for observer in self._observers:
                observer.update(self)
        else:
            logger.info('No subscribed observers.')

    def send_discounts(self) -> None:
        """Usually, the subscription logic is only a fraction of what a Subject can really do.

        Subjects commonly hold some important business logic, that triggers a notification method whenever something
        important is about to happen (or after it).
        """
        logger.info("Subject: I'm checking available discounts.")
        week_day_number = datetime.now(tz=pytz.timezone('Europe/Vienna')).weekday()
        self._state = 'workday' if week_day_number < 5 else 'weekend'
        logger.info(f'Subject: My state has just changed to: {self._state}')
        self.notify()


class Observer(ABC):
    """The Observer interface declares the update method, used by subjects."""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Receive update from subject."""


"""Concrete Observers react to the updates issued by the Subject they had been attached to."""


class ObserverWorkDayDiscounts(Observer):
    """Update subscribed customer on work day discounts."""

    def update(self, subject: Subject) -> None:
        """Inform observer about discounts."""
        if subject.state == 'workday':
            logger.info(r'This week latte coffee has 50% discount')


class ObserverWeekendDiscounts(Observer):
    """Update subscribed customers on weekend discount."""

    def update(self, subject: Subject) -> None:
        """Inform observer about discounts."""
        if subject.state == 'weekend':
            logger.info(r'This weekend cappuccino coffee has 30% discount')
