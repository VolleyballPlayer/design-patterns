import pytest

from designpatterns.behavioral_patterns.command import Invoker, OrderCommand, PrepareCoffeeCommand, Receiver
from designpatterns.helpers.receipts import Receipt, latte_receipt


class TestCommand:
    def test__run_command__(self, caplog: pytest.LogCaptureFixture) -> None:
        invoker = Invoker()
        invoker.set_on_start(OrderCommand(latte_receipt))
        receiver = Receiver()
        invoker.set_on_finish(PrepareCoffeeCommand(receiver, latte_receipt, 'John Smith'))
        invoker.execute_commands_in_order()
        assert 'receiving order for latte coffee' in caplog.text
        assert 'Receiver: Preparing latte' in caplog.text
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text
