import pytest

from designpatterns.creational_patterns.singleton import CountCoffeeSingleton


class TestSingleton:
    def test_count(self, caplog: pytest.LogCaptureFixture) -> None:
        s1 = CountCoffeeSingleton()
        s2 = CountCoffeeSingleton()

        s1.count()
        s2.count()

        assert id(s1) == id(s2)
        assert '4. coffee is being prepared' in caplog.text
        assert '5. coffee is being prepared' in caplog.text
