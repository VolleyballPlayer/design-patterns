import pytest

from designpatterns.behavioral_patterns.mediator import Coffee, ConcreteMediator, Order, Payment
from designpatterns.helpers.receipts import latte_receipt


class TestMediator:
    def test__run_mediator__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        mediator = ConcreteMediator()

        order = Order(mediator)
        coffee = Coffee(mediator)
        payment = Payment(mediator)

        mediator.add_component(order)
        mediator.add_component(coffee)
        mediator.add_component(payment)

        mediator.notify()
        order.process(coffee=latte_receipt.name)
        coffee.prepare(coffee=latte_receipt.name)
        payment.receive(coffee=latte_receipt.name)

        assert 'Order is ready' in caplog.text
        assert 'Coffee is ready' in caplog.text
        assert 'Payment is processed' in caplog.text
        assert 'Receiving order for latte coffee' in caplog.text
        assert 'Preparing latte coffee' in caplog.text
        assert 'Receiving payment for latte coffee' in caplog.text
