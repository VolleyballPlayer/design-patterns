import pytest

from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt
from designpatterns.structural_patterns.proxy import Coffee, Proxy, client_code


class TestProxy:
    def test__run_proxy__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        real_subject = Coffee()
        client_code(real_subject, latte_receipt)
        proxy = Proxy(real_subject)
        client_code(proxy, latte_receipt)
        client_code(proxy, cappuccino_receipt)
        client_code(proxy, latte_receipt)

        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text
        assert Receipt.get_coffee(receipt=cappuccino_receipt) in caplog.text
        for text in [
            'Latte was already prepared.',
            'Proxy: Logging the time of request',
            'Proxy: Checking if subject instance already exists to reuse cached instance.',
        ]:
            assert text in caplog.text
