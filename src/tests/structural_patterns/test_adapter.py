import pytest

from designpatterns.helpers.receipts import latte_receipt
from designpatterns.structural_patterns.adapter import Adaptee, Adapter, Target, client_code


class TestAdapter:
    def test__run_adapter__get_expected_output(self, capsys: pytest.CaptureFixture[str]) -> None:
        target = Target()
        client_code(target)
        adaptee = Adaptee(latte_receipt)
        adaptee.get_coffee()
        adapter = Adapter(adaptee)
        client_code(adapter)
        captured = capsys.readouterr()
        assert latte_receipt.name in captured.out
        assert latte_receipt.coffee in captured.out
        assert latte_receipt.milk in captured.out
        assert latte_receipt.milk_foam in captured.out
