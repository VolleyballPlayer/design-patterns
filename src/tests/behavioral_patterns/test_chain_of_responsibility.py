import pytest

from designpatterns.behavioral_patterns.chain_of_responsibility import (
    CakeHandler,
    CoffeeHandler,
    TeaHandler,
    client_code,
)


class TestChainOfResponsibility:
    def test__run_chain_of_responsibitily__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        coffee = CoffeeHandler()
        cake = CakeHandler()
        tea = TeaHandler()

        coffee.set_next(cake).set_next(tea)

        client_code(coffee)
        client_code(cake)
        client_code(tea)

        for log_message in [
            'Tea gets honey',
            'Coffee gets water',
            'Coffee gets sugar',
            'Tea gets water',
            'sugar was left unused. There is no product that needs it.',
            'Cake gets sugar',
        ]:
            assert log_message in caplog.text
