import pytest

from designpatterns.creational_patterns.factory_method import (
    CappuccinoCreator,
    EspressoCreator,
    LatteCreator,
    client_code,
)
from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, espresso_receipt, latte_receipt


class TestFactoryMethod:
    def test__run_factory_method__prepared_latte(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(LatteCreator())
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text

    def test__run_factory_method__prepared_cappuccino(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(CappuccinoCreator())
        assert Receipt.get_coffee(cappuccino_receipt) in caplog.text

    def test__run_factory_method__prepared_espresso(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(EspressoCreator())
        assert Receipt.get_coffee(espresso_receipt) in caplog.text
