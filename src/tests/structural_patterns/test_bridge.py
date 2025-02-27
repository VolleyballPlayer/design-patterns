import pytest

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt
from designpatterns.structural_patterns.bridge import Abstraction, Cappuccino, Coffee, Latte, client_code


class TestBridge:
    def test__run_bridge__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        implementation = Latte()
        abstraction = Abstraction(implementation)
        client_code(abstraction)

        print('\n')

        implementation = Cappuccino()
        abstraction = Coffee(implementation)
        client_code(abstraction)

        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text
        assert Receipt.get_coffee(receipt=cappuccino_receipt) in caplog.text
        assert 'Abstraction: Base operation with:' in caplog.text
        assert 'ExtendedAbstraction: Extended operation with:' in caplog.text
