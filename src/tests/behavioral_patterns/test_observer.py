from datetime import datetime

import pytest
import pytz

from designpatterns.behavioral_patterns.observer import (
    DiscountSubject,
    ObserverWeekendDiscounts,
    ObserverWorkDayDiscounts,
)


class TestObserver:
    def test__run_observer__get_notifications_on_workdays(self, caplog: pytest.LogCaptureFixture) -> None:
        subject = DiscountSubject()
        observer_workday = ObserverWorkDayDiscounts()
        subject.attach(observer_workday)
        observer_weekend = ObserverWeekendDiscounts()
        subject.attach(observer_weekend)
        subject.send_discounts()
        subject.detach(observer_workday)
        subject.detach(observer_weekend)
        week_day_number = datetime.now(tz=pytz.timezone('Europe/Vienna')).weekday()
        if week_day_number < 5:
            assert r'This week latte coffee has 50% discount' in caplog.text
        else:
            assert r'This weekend cappuccino coffee has 30% discount' in caplog.text

    def test__detach_observer__info_no_observers(self, caplog: pytest.LogCaptureFixture) -> None:
        subject = DiscountSubject()
        observer = ObserverWorkDayDiscounts()
        subject.attach(observer)
        subject.detach(observer)
        subject.send_discounts()
        assert 'No subscribed observers.' in caplog.text
