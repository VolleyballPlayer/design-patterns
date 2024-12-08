import pytest

from designpatterns.creational_patterns.singleton import CountCoffeeSingleton


class TestSingleton:
    def test__count__get_logs_per_number(self, caplog: pytest.LogCaptureFixture) -> None:
        s1 = CountCoffeeSingleton()
        s2 = CountCoffeeSingleton()

        s1.count()
        s2.count()

        assert id(s1) == id(s2)
        assert '5. coffee is being prepared' in caplog.text
        assert '6. coffee is being prepared' in caplog.text
