import pytest

from designpatterns.helpers.receipts import Receipt, latte_receipt
from designpatterns.structural_patterns.decorator import Notification, Payment, PrepareLatte, client_code


class TestDecorator:
    def test__run_decorator__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        coffee = PrepareLatte()
        client_code(coffee)
        decorator1 = Notification(coffee)
        client_code(decorator1)
        decorator2 = Payment(decorator1)
        client_code(decorator2)

        assert 'Latte is prepared' in caplog.text
        assert 'Your coffee costs €5. Do you want to pay by cash or card?' in caplog.text
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text

    def test__getter__get_component(self) -> None:
        coffee = PrepareLatte()
        decorator1 = Notification(coffee)
        assert isinstance(decorator1.component, PrepareLatte) is True
