import pytest

from designpatterns.structural_patterns.flyweight import FlyweightFactory, add_coffee_to_order_list


class TestFlyweight:
    def test__run_flyweight__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        factory = FlyweightFactory([['latte'], ['cappuccino']])
        factory.list_flyweights()
        add_coffee_to_order_list(factory, 'latte', 'Ema')
        add_coffee_to_order_list(factory, 'espresso', 'Diana')
        factory.list_flyweights()

        log_messages = [
            'FlyweightFactory: I have 2 flyweights',
            'Client: Adding an ordered latte coffee',
            'Client: Adding an ordered espresso coffee',
            'FlyweightFactory: I have 3 flyweights',
        ]
        for message in log_messages:
            assert message in caplog.text
