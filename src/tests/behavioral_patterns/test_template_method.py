import pytest

from designpatterns.behavioral_patterns.template_method import Cappuccino, Latte, client_code
from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt


class TestTemplateMethod:
    GET_COFFEE_ORDER = 'Automat says: I am receiving coffee order'
    ASSIGN_ORDER_TO_EMPLOYEE = 'Automat says: Your order will be prepared by Maria'
    FINALIZE_ORDER = 'Automat says: Your order is ready'

    def test__run_template_method__get_latte_output(self, caplog: pytest.LogCaptureFixture) -> None:
        client_code(Latte())
        assert TestTemplateMethod.GET_COFFEE_ORDER in caplog.text
        assert TestTemplateMethod.ASSIGN_ORDER_TO_EMPLOYEE in caplog.text
        assert TestTemplateMethod.FINALIZE_ORDER in caplog.text
        assert 'Your latte order is being prepared' in caplog.text
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text

    def test__run_template_method__get_cappuccino_output(self, caplog: pytest.LogCaptureFixture) -> None:
        Cappuccino().template_method()
        assert TestTemplateMethod.GET_COFFEE_ORDER in caplog.text
        assert TestTemplateMethod.ASSIGN_ORDER_TO_EMPLOYEE in caplog.text
        assert TestTemplateMethod.FINALIZE_ORDER in caplog.text
        assert 'Your cappuccino order is being prepared' in caplog.text
        assert 'Maria forwarded order to a colleague Pedro' in caplog.text
        assert Receipt.get_coffee(receipt=cappuccino_receipt) in caplog.text
