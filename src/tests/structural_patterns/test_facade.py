import pytest

from designpatterns.behavioral_patterns.command import Receiver
from designpatterns.helpers.receipts import latte_receipt
from designpatterns.structural_patterns.facade import (
    ExtendedOrderCommand,
    ExtendedPrepareCoffeeCommand,
    Facade,
    client_code,
)


class TestFacade:
    def test__run_facade__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        subsystem1 = ExtendedOrderCommand(latte_receipt)
        subsystem2 = ExtendedPrepareCoffeeCommand(Receiver(), latte_receipt, 'John Smith')
        facade = Facade(subsystem1, subsystem2)
        client_code(facade)
        assert 'Facade initializes subsystems' in caplog.text
        assert 'Facade orders subsystems to perform the action' in caplog.text
        assert 'Your coffee costs €2. This is your bill' in caplog.text
