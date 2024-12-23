import pytest

from designpatterns.creational_patterns.abstract_factory import (
    CappuccinoFactory,
    EspressoFactory,
    LatteFactory,
    client_code_abstract_factory,
)
from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, espresso_receipt, latte_receipt


class TestFactoryMethod:
    def test__run_factory_method__prepared_latte(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code_abstract_factory(LatteFactory())
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text

    def test__run_factory_method__prepared_cappuccino(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code_abstract_factory(CappuccinoFactory())
        assert Receipt.get_coffee(cappuccino_receipt) in caplog.text

    def test__run_factory_method__prepared_espresso(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code_abstract_factory(EspressoFactory())
        assert Receipt.get_coffee(espresso_receipt) in caplog.text
