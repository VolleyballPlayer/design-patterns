import pytest

from designpatterns.creational_patterns.factory_method import (
    CappuccinoCreator,
    EspressoCreator,
    LatteCreator,
    client_code,
)
from designpatterns.helpers.receipts import cappuccino_receipt, espresso_receipt, latte_receipt


class TestFactoryMethod:
    def test__run_factory_method__prepared_latte(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(LatteCreator())
        assert latte_receipt.get_coffee() in caplog.text

    def test__run_factory_method__prepared_cappuccino(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(CappuccinoCreator())
        assert cappuccino_receipt.get_coffee() in caplog.text

    def test__run_factory_method__prepared_espresso(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(EspressoCreator())
        assert espresso_receipt.get_coffee() in caplog.text
